from openpyxl import load_workbook
import requests
import os
import time
import json
from dsyWebAPI.dsy.common.httpMethod import httpRequest
from dsyWebAPI.dsy.common.mapDict import switchDict, dataDict
from dsyWebAPI.dsy.common.changeValue import getChangeValue, replaceValue
from dsyWebAPI.dsy.common.configLog import Log
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class excel():
    def __init__(self):
        self.mylogger = Log().get_logger()
        self.excelPath = os.path.join(os.getcwd().split('dsyWebAPI')[0], 'dsyWebAPI\\dsy\\case', 'TestCaseFile.xlsx')
        self.wb = load_workbook(filename=self.excelPath, data_only=True)
        self.case_sheet = self.wb.get_sheet_by_name('case')
        self.login_url = 'https://dsylogin.10333.com'  # 登录界面url
        self.sys_url = 'http://dsyjg.10333.com'  # 登录之后url
        self.headers = {
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh-CN,zh;q=0.9",
            'content-type': "application/x-www-form-urlencoded"
        }
        self.changeValue_dict = {}
    def case(self):
        for active in self.case_sheet['C']:
            if active.value == 'yes':
                '''
                A用例编号，B模块名称，C是否执行，D用例名称，E请求路径url，F请求方法，
                G替换的参数ID，H参数，I上传文件参数，J预期结果，K检查点，L实际返回结果，M传递参数ID，N传递目标参数ID，O备注
                '''
                CaseName = self.case_sheet['D' + str(active.row)].value
                self.mylogger.info("执行第" + str(active.row) + "行--" + CaseName + "用例")
                url = self.case_sheet['E' + str(active.row)].value.strip()
                Method =self.case_sheet['F' + str(active.row)].value.strip()
                ReplaceID = self.case_sheet['G' + str(active.row)].value
                Data = dataDict.data_dict(self.case_sheet['H' + str(active.row)].value)
                Files = self.case_sheet['I' + str(active.row)].value
                Except = self.case_sheet['J' + str(active.row)].value
                CheckPoint = self.case_sheet['K' + str(active.row)].value
                # 获取Result、Remark单元格坐标
                # Result = self.case_sheet['L' + str(active.row)]
                TransmitID = self.case_sheet['M' + str(active.row)].value
                TransmitTargetID = self.case_sheet['N' + str(active.row)].value
                # Remark = self.case_sheet['O' + str(active.row)]

                # 找到login标识, 0 为找到了，-1 为没找到
                if CaseName.find('login') == 0:  # 找到"login"
                    url = ''.join((self.login_url, url))
                    login = httpRequest().send_request(url=url, method=Method, headers=self.headers, verify=False)
                    try:
                        cookie_jar = login.request._cookies
                        requests.utils.dict_from_cookiejar(cookie_jar)
                        USERID_SID = cookie_jar['USERID_SID']
                        self.headers['Cookie'] = 'USERID_SID=' + USERID_SID
                        self.mylogger.info("登录成功")
                        self.case_sheet['O' + str(active.row)] = 'true'
                    except Exception as e:
                        self.mylogger.error("登录失败", e)
                        pass
                else:
                    url = ''.join((self.sys_url, url))
                    if ReplaceID is not None:
                        self.mylogger.info("更新动态ID")
                        try:
                            replaceValue.replace_value(ReplaceID.strip(), Data, self.changeValue_dict)
                            self.mylogger.info(Data)
                            self.mylogger.info("更新Data动态ID完成")
                        except Exception as e:
                            self.mylogger.error("更新Data动态ID失败", e)
                    if Files is not None:
                        # 上传文件content-type =  multipart/form-data
                        self.headers.pop('content-type')
                        files = eval(Files)
                        response = httpRequest().send_request(url=url, method=Method, headers=self.headers, data=None, files=files, verify=False)
                        self.headers['content-type'] = "application/x-www-form-urlencoded"
                    else:
                        response = httpRequest().send_request(url=url, method=Method, headers=self.headers, params=Data, data=Data, verify=False)

                    if TransmitID is not None:
                        try:
                            getChangeValue.parse_response(response.json(), TransmitID.strip(), TransmitTargetID.strip(), self.changeValue_dict)
                            self.mylogger.info("--------------------提取动态ID完成---------------------")
                            self.mylogger.info(getChangeValue.parse_response(response.json(), TransmitID, TransmitTargetID, self.changeValue_dict))
                        except Exception as e:
                            self.mylogger.error("提取动态ID失败", e)
                    self.mylogger.info('-----------------' + str(response.json()))
                    self.case_sheet['L' + str(active.row)] = str(response.json())  # 将response写入到Result单元格中
                    self.mylogger.info("解析返回的json中")
                    Result = switchDict.dict(response.json())
                    Except = switchDict.dict(Except)
                    self.mylogger.info("解析返回的json完成")
                    result = []
                    expectation = []
                    self.mylogger.info("对比结果中")
                    for checkPoint in CheckPoint.split(','):
                        result.append(Result[checkPoint])
                        expectation.append(Except[checkPoint])
                    if result == expectation:
                        self.case_sheet['O' + str(active.row)] = 'true'
                        self.mylogger.info("对比完成，结果为“true”")
                    else:
                        self.case_sheet['O' + str(active.row)] = 'false'
                        self.mylogger.info("对比完成，结果为“false”")
                    del result[:]
                    del expectation[:]
        reportName = time.strftime('%Y-%m-%d %H-%M-%S')+'caseResult.xlsx'
        self.excelReportPath = os.path.join(os.getcwd().split('dsyWebAPI')[0], 'dsyWebAPI\\dsy\\report', reportName)
        self.wb.save(self.excelReportPath)
        self.mylogger.info("保存excel")
        self.wb.close()
        self.mylogger.info("关闭excel")


if __name__ == '__main__':
    caseValue = excel().case()

import requests

class httpRequest:
    def __get(self, url, params, **kwargs):
        return requests.get(url, params, **kwargs)

    def __post(self, url, data=None, json=None, **kwargs):
        return requests.post(url, data, json, **kwargs)

    def send_request(self, url, method, params=None, data=None, json=None, **kwargs):
        if method == "get" or method == "GET":
            response = self.__get(url=url, params=params, **kwargs)
            return response
        elif method == "post" or method == "POST":
            response = self.__post(url=url, data=data, json=json, **kwargs)
            return response


if __name__ == '__main__':
    from requests.packages import urllib3
    urllib3.disable_warnings()
    url = "https://dsylogin.10333.com/dotoyo/register/goDsySubsystem.do?username=13744444081&sysType=1"
    headers = {

        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',

    }
    r1 = httpRequest().send_request(url=url, headers=headers, method="get", verify=False)
    # a.encoding = 'utf-8'
    # print(a.text)
    cookie_jar = r1.request._cookies
    requests.utils.dict_from_cookiejar(cookie_jar)
    USERID_SID = cookie_jar['USERID_SID']
    headers['Cookie'] = 'USERID_SID=' + USERID_SID
    url2 = "http://dsyjg.10333.com/uploadFiles/uploadBigFile"
    files = {
        'id': (None, 'WU_FILE_1'),
        'name': (None, "xpath.jpg"),
        'chunkMD5': (None, "blockmd5"),
        "Filedata": ("xpath.jpg", open("C:\\Users\\Grunmi\\Desktop\\xpath.jpg", "rb").read(), 'image/jpeg')
    }
    multiple_files = {'id': (None, 'WU_FILE_1'),
                      'name': (None, "xpath.jpg"),
                      'chunkMD5': (None, "blockmd5"),
                      'Filedata': ('xpath.jpg', open('C:\\Users\\Grunmi\\Desktop\\xpath.jpg', 'rb'), 'image/jpeg')}

    # data = {"uploadType":"default","busiName":"attachment","userId":"371c6107d3ca4d7090f5273eecfdb746","currentUserName":"53103","currentOrgId":"4028814a5d8de01f015d96fd68ab0027","currentCompanyId":"402881495d8dcdf8015d967fbd080000","cityId":"undefined"}
    # r2 = httpRequest().send_request(url=url2, headers=headers,  method='POST', files=multiple_files, verify=False)
    r2 = httpRequest().send_request(url=url2, method='POST', headers=headers, data=None, files=multiple_files, verify=False)
    print(r2.status_code)
    # print(r2.text)
    response = (r2.json())
    print(type(response), response)



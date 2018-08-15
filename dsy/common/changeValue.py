from dsyWebAPI.dsy.common.mapDict import dataDict
class getChangeValue:
    @staticmethod
    def parse_response(response, TransmitID, TransmitTargetID, changeValue_dict):
        TransmitValueID = []  # 传递参数ID
        TransmitTargetValueID = []    # 传递目标参数ID
        for Transmit in TransmitID.split(','):
            TransmitValueID.append(Transmit.strip())
        for TransmitTarget in TransmitTargetID.split(','):
            TransmitTargetValueID.append(TransmitTarget.strip())
        if len(TransmitValueID) == len(TransmitTargetValueID):
            for index in range(len(TransmitValueID)):
                for k1, v1 in response.items():
                    if isinstance(k1, int) and k1 == int(TransmitValueID[index]):
                        changeValue_dict[TransmitTargetValueID[index]] = response[int(TransmitValueID[index])]
                    elif k1 == TransmitValueID[index]:
                        changeValue_dict[TransmitTargetValueID[index]] = response[TransmitValueID[index]]
                    elif isinstance(v1, dict):
                        for k2, v2 in v1.items():
                            if k2 == TransmitValueID[index]:
                                changeValue_dict[TransmitTargetValueID[index]] = v1[TransmitValueID[index]]
                            elif isinstance(v2, dict):
                                for k3, v3 in v2.items():
                                    if k3 == TransmitValueID[index]:
                                        changeValue_dict[TransmitTargetValueID[index]] = v2[TransmitValueID[index]]
                                    elif isinstance(v3, dict):
                                        for k4, v4 in v3.items():
                                            if k4 == TransmitValueID[index]:
                                                changeValue_dict[TransmitTargetValueID[index]] = v3[TransmitValueID[index]]
            return changeValue_dict


class replaceValue:
    @staticmethod
    def replace_value(ReplaceID,Data,changeValue_dict):
        replaceValueID = []
        for replace in ReplaceID.split(','):
            replaceValueID.append(replace.strip())
        # if isinstance(Data, str):
        #     Data = dataDict.data_dict(Data)
        for replaceValue in replaceValueID:
            for k1, v1 in Data.items():
                if k1 == replaceValue and v1 == "#":
                    Data[k1] = changeValue_dict[replaceValue]
                if isinstance(v1, dict):
                    for k2, v2 in v1.items():
                        if k2 == replaceValue and v2 == "#":
                            v1[k2] = changeValue_dict[replaceValue]
                        elif isinstance(v2, dict):
                            for k3, v3 in v2.items():
                                if k3 == replaceValue and v3 == "#":
                                    v2[k3] = changeValue_dict[replaceValue]
            return Data

if __name__ == '__main__':
    # response={1:1,'2':2}
    # TransmitID='1,2'
    # TransmitTargetID='3,4'
    # changeValue_dict = {}
    # a = getChangeValue.parse_response(response,TransmitID,TransmitTargetID,changeValue_dict)
    # print(a)
    # print(changeValue_dict)
    # ReplaceID='4,3'
    # Data="{'4': '#','3':'#'}"
    # # changeValue_dict = {'4': 2}
    # b = replaceValue.replace_value(ReplaceID,Data,changeValue_dict)
    # print(b)
    # response = {'r': 1, 'h': False, 'm': '操作成功', 'd': {'diary': {'name': '2017年11月23日(星期四)监理日记', 'week': '星期四', 'weather': {'tempMin': 13, 'tempMax': 19, 'windGrade': '4', 'id': '4028814a5fd8f68d015fe475389801f2', 'windSc': '微风', 'weatherCond': '多云', 'windDir': '无持续风向'}}, 'reviewUsers': [{'roleId': 'e6d1b5b2d87943a7938510372a1505ab', 'roleName': '总监理工程师', 'userId': '402881495d8dd5d5015d97134d18004f', 'userName': '刘星9'}], 'modules': 'SGENVIRONMENT,SGPROGRESS,MATERIALENTER,WITNESSCHECK,EQUIPMENTENTER,SUPERVISION,QUALITYVIEWCHECK,SECURITYVIEWCHECK,QUALITYACCEPT,SECURITYACCEPT,INVEST,PROGRESSVIEWCHECK,OTHER', 'lastreviewuser': {'roleId': None, 'other': 1, 'reviewUserId': '144d06d9f6f44a658574e0581f8406de'}, 'modulesContent': {'SUPERVISION': [{'sgzName': '哈工大施工总包二工程', 'endDate': 1511430060000, 'visionUserName': '监理一号', 'startDate': 1511430060000, 'sgzEntName': '巴州峰源鑫达混凝土有限公司', 'sgzId': '4028814a5d8de01f015d96fd68ab0027', 'sgfId': '4028814a5d8de01f015d9700ec0a0029', 'startDateFmt': '2017-11-23 17:41', 'sgfEntName': '新疆瀚宇建筑工程有限责任公司', 'code': '0069', 'userId': '144d06d9f6f44a658574e0581f8406de', 'sgfName': '哈工大施工分包二', 'processName': '33', 'endDateFmt': '2017-11-23 17:41', 'unitId': '4028814d5f231eba015f326ef53f02f1', 'attsList': [{'name': 'C5B8F0E2-6031-4B9D-A1DB-4B89433E5810.jpg', 'size': 52, 'type': 'jpg', 'url': 'http://dsyfile.10333.com//attachment/4028814a5d8de01f015d9693f1420012/2017/11/23/689EE18B-8550-4895-94BD-481F6FBE098F.jpg', 'id': '4028814a5fa52f44015fe841bb34338d', 'reZipUrl': None, 'queryUrl': None}, {'name': 'B1A00EAF-E776-4D8E-AF09-5CD49ECFD4E0.jpg', 'size': 52, 'type': 'jpg', 'url': 'http://dsyfile.10333.com//attachment/4028814a5d8de01f015d9693f1420012/2017/11/23/2EF35807-9814-4B8F-9B64-7706D037AE60.jpg', 'id': '4028814d5f6cc86b015fe841b9c05245', 'reZipUrl': None, 'queryUrl': None}, {'name': 'A7B7BD6F-9AC8-4A77-9A18-FE9D03182E07.jpg', 'size': 50, 'type': 'jpg', 'url': 'http://dsyfile.10333.com//attachment/4028814a5d8de01f015d9693f1420012/2017/11/23/DECAF815-2EA5-499F-8D11-2D5C47601289.jpg', 'id': '4028814d5f6cc86b015fe841bc1e5246', 'reZipUrl': None, 'queryUrl': None}], 'unitName': '1019地下室（A区）'}], 'QUALITYVIEWCHECK': [], 'QUALITYACCEPT': {'itemAccept': [], 'lotAccept': []}, 'MATERIALENTER': [], 'SECURITYVIEWCHECK': [], 'INVEST': [], 'WITNESSCHECK': [], 'EQUIPMENTENTER': [], 'SECURITYACCEPT': []}, 'dailyFlag': False}}
    # TransmitID = "reviewUserId,id"
    # TransmitTargetID = "reviewUserId,weatherId"
    # print(getChangeValue.parse_response(response,TransmitID,TransmitTargetID,changeValue_dict))
    changeValue_dict={'reviewUserId': '13a96f628ec946149aeb87052f2b2c28', 'weatherId': '4028814d5fd8f6c501600881b3a30790'}
    ReplaceID = "reviewUserId,weatherId,reviewUserId"
    Data = "data={'diary':{'id':'','operate':'submit','type':'SGDIARY','diaryDate':'2017-11-30','name':'2017年11月30日(星期四)施工日记','reviewUserId':'#','remark':'','week':'星期四','other':1,'reviewUserName':'施工总包一号（哈工大施工总包二工程-项目管理员）','updateDiary':false,'weatherId':'#'},'modules':'SGENVIRONMENT,PRODUCTION,QUALITYCHECK,SECURITYCHECK,MATERIALENTER,WITNESSCHECK,EQUIPMENTENTER,QUALITYACCEPT,SECURITYACCEPT,OTHER','modulesContent':'{\'SGENVIRONMENT\':[{\'changed\':1,\'content\':\'\',\'attaIds\':\'\',\'enter\':0}],\'PRODUCTION\':[{\'changed\':1,\'checkPoint\':\'\',\'personArrange\':\'\',\'machineArrange\':\'\',\'materialUse\':\'\',\'problemHandle\':\'\',\'attaIds\':\'\',\'enter\':0}],\'QUALITYCHECK\':[],\'SECURITYCHECK\':[],\'MATERIALENTER\':[],\'WITNESSCHECK\':[],\'EQUIPMENTENTER\':[],\'QUALITYACCEPT\':{\'itemAccept\':[],\'lotAccept\':[]},\'SECURITYACCEPT\':[],\'OTHER\':[{\'changed\':1,\'content\':\'\',\'attaIds\':\'\',\'enter\':0}]}','lastreviewuser':{'reviewUserId':'#','roleId':null,'other':0},'dailyFlag':false}"
    print(replaceValue.replace_value(ReplaceID,Data,changeValue_dict))
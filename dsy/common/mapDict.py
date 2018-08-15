import json
from urllib.parse import urlencode


class switchDict:
    @staticmethod
    def dict(old_dict):
        new_dict = {}
        key = []
        value = []
        if isinstance(old_dict, str):
            if 'false' in old_dict or 'true' in old_dict or 'null' in old_dict:
                old_dict = old_dict.replace('false', 'False')
                old_dict = old_dict.replace('true', 'True')
                old_dict = old_dict.replace('null', 'None')
                # old = json.loads(json.dumps(old_dict))
                try:
                    # "{'a':'b'}"
                    old = eval(old_dict)
                    for k1, v1 in old.items():
                        key.append(k1)
                        value.append(v1)
                        if isinstance(v1, dict):
                            for k2, v2 in v1.items():
                                key.append(k2)
                                value.append(v2)
                                # dict里面存在list，list里面包含多个dict,并且key值相同情况下需要与之前的key的list做比较，字典key不能相同
                                if isinstance(v2, list):
                                    switchDict.listInsideDict(v2,key,value)
                                # dict里面存在dict
                                elif isinstance(v2, dict):
                                    switchDict.dictInsideDict(v2,key,value)
                        elif isinstance(v1, list):
                            switchDict.listInsideDict(v1,key,value)
                        new_dict.update(dict(zip(key, value)))
                except:
                    pass
        # "[{'a':'b'}]"
        elif isinstance(old_dict, list):
            old_dict = str(old_dict)
            if old_dict[:1] == "[":
                b = old_dict.replace(old_dict[0], '')
                c = b.replace(b[-1], '')
                return eval(c)
        elif isinstance(old_dict, dict):
            for k1, v1 in old_dict.items():
                key.append(k1)
                value.append(v1)
                if isinstance(v1, dict):
                    for k2, v2 in v1.items():
                        key.append(k2)
                        value.append(v2)
                        # dict里面存在list，list里面包含多个dict,并且key值相同情况下需要与之前的key的list做比较，字典key不能相同
                        if isinstance(v2, list):
                            switchDict.listInsideDict(v2,key,value)
                        # dict里面存在dict
                        elif isinstance(v2, dict):
                            switchDict.dictInsideDict(v2, key, value)
                elif isinstance(v1, list):
                    switchDict.listInsideDict(v1,key,value)
                new_dict.update(dict(zip(key, value)))
        return new_dict

    @staticmethod
    def listInsideDict(list, key_list, value_list):
        list_dicts = []
        for index in range(len(list)):
            if isinstance(list[index], dict):
                list_dicts.append(list[index])
                for list_dict in list_dicts:
                    if isinstance(list_dict, dict):
                        for k, v in list_dict.items():
                            # 判断key值是否有一样的，存在一样则加上index
                            if k not in key_list:
                                key_list.append(k)
                                value_list.append(v)
                            else:
                                key_list.append(k + str(index))
                                value_list.append(v)

    @staticmethod
    def dictInsideDict(dict_value, key_list, value_list):
        index = 1
        for k, v in dict_value.items():
            if k not in key_list:
                key_list.append(k)
                value_list.append(v)
            else:
                key_list.append(k + str(index))
                value_list.append(v)
                index += index



class dataDict:
    @staticmethod
    def data_dict(old_data):
        if old_data==None:
            return None
        else:
            # if 'false' in old_data or 'true' in old_data or 'null' in old_data:
            #     old_data = old_data.replace('false', 'False')
            #     old_data = old_data.replace('true', 'True')
            #     old_data = old_data.replace('null', 'None')
            if '&' in old_data and '=' in old_data:
                new_data = {}
                for data in old_data.split('&'):
                    result = [data.strip() for data in data.split('=')]
                    new_data.update(dict([result]))
                return urlencode(new_data)
            elif '&' not in old_data and '=' in old_data:
                new_data = {}
                result = [data.strip() for data in old_data.split('=')]
                new_data.update(dict([result]))
                return urlencode(new_data)
            else:
                data = eval(old_data)
                # safe 表示什么字符不编码， （） 表示所有的不编码
                new_data = urlencode(data, safe="()")
                return new_data



if __name__ == '__main__':
    # a = {1:False}
    # print(switchDict.dict(a))
    # b = '{"r":1,"m":"操作成功","h":false,"d":{"user":{"id":"144d06d9f6f44a658574e0581f8406de","realName":"监理一号","headPhoto":None,"identificationCard":"452158232326585622","mobile":"13711111022"}}}'
    # print(switchDict.dict(b))
    # bb='{"data":"{"diary":{"id":"","operate":"submit","type":"SGDIARY","diaryDate":"2017-11-30","name":"2017年11月30日(星期四)施工日记","reviewUserId":"13a96f628ec946149aeb87052f2b2c28","remark":"","week":"星期四","other":1,"reviewUserName":"施工总包一号（哈工大施工总包二工程-项目管理员）","updateDiary":false,"weatherId":"4028814d5fd8f6c501600881b3a30790"},"modules":"SGENVIRONMENT,PRODUCTION,QUALITYCHECK,SECURITYCHECK,MATERIALENTER,WITNESSCHECK,EQUIPMENTENTER,QUALITYACCEPT,SECURITYACCEPT,OTHER","modulesContent":"{\"SGENVIRONMENT\":[{\"changed\":1,\"content\":\"\",\"attaIds\":\"\",\"enter\":0}],\"PRODUCTION\":[{\"changed\":1,\"checkPoint\":\"\",\"personArrange\":\"\",\"machineArrange\":\"\",\"materialUse\":\"\",\"problemHandle\":\"\",\"attaIds\":\"\",\"enter\":0}],\"QUALITYCHECK\":[],\"SECURITYCHECK\":[],\"MATERIALENTER\":[],\"WITNESSCHECK\":[],\"EQUIPMENTENTER\":[],\"QUALITYACCEPT\":{\"itemAccept\":[],\"lotAccept\":[]},\"SECURITYACCEPT\":[],\"OTHER\":[{\"changed\":1,\"content\":\"\",\"attaIds\":\"\",\"enter\":0}]}","lastreviewuser":{"reviewUserId":"13a96f628ec946149aeb87052f2b2c28","roleId":null,"other":0},"dailyFlag":false}"}'
    # print(bb)
    # print(dataDict.data_dict(bb))
    cc = "data={'2':'3','2':'4'}"
    dd="data={'diary':{'id':'','operate':'submit','type':'SGDIARY','diaryDate':'2017-11-30','name':'2017年11月30日(星期四)施工日记','reviewUserId':'13a96f628ec946149aeb87052f2b2c28','remark':'','week':'星期四','other':1,'reviewUserName':'施工总包一号（哈工大施工总包二工程-项目管理员）','updateDiary':false,'weatherId':'4028814d5fd8f6c501600881b3a30790'},'modules':'SGENVIRONMENT,PRODUCTION,QUALITYCHECK,SECURITYCHECK,MATERIALENTER,WITNESSCHECK,EQUIPMENTENTER,QUALITYACCEPT,SECURITYACCEPT,OTHER','modulesContent':'{\'SGENVIRONMENT\':[{\'changed\':1,\'content\':\'\',\'attaIds\':\'\',\'enter\':0}],\'PRODUCTION\':[{\'changed\':1,\'checkPoint\':\'\',\'personArrange\':\'\',\'machineArrange\':\'\',\'materialUse\':\'\',\'problemHandle\':\'\',\'attaIds\':\'\',\'enter\':0}],\'QUALITYCHECK\':[],\'SECURITYCHECK\':[],\'MATERIALENTER\':[],\'WITNESSCHECK\':[],\'EQUIPMENTENTER\':[],\'QUALITYACCEPT\':{\'itemAccept\':[],\'lotAccept\':[]},\'SECURITYACCEPT\':[],\'OTHER\':[{\'changed\':1,\'content\':\'\',\'attaIds\':\'\',\'enter\':0}]}','lastreviewuser':{'reviewUserId':'13a96f628ec946149aeb87052f2b2c28','roleId':null,'other':0},'dailyFlag':false}"
    ee=str({'data':"{'diary':{'id':'','operate':'submit','type':'SGDIARY','diaryDate':'2017-12-01','name':'2017年12月01日(星期五)施工日记','reviewUserId':'13a96f628ec946149aeb87052f2b2c28','remark':'','week':'星期五','other':1,'reviewUserName':'施工总包一号（哈工大施工总包二工程-项目管理员）','updateDiary':false,'weatherId':'4028814d5fd8f6c501600da81af9080d'},'modules':'PRODUCTION,QUALITYCHECK,SECURITYCHECK,MATERIALENTER,WITNESSCHECK,EQUIPMENTENTER,QUALITYACCEPT,SECURITYACCEPT,OTHER,SGENVIRONMENT','modulesContent':'{\'PRODUCTION\':[{\'changed\':1,\'checkPoint\':\'\',\'personArrange\':\'\',\'machineArrange\':\'\',\'materialUse\':\'\',\'problemHandle\':\'\',\'attaIds\':\'\',\'enter\':0}],\'QUALITYCHECK\':[],\'SECURITYCHECK\':[],\'MATERIALENTER\':[],\'WITNESSCHECK\':[],\'EQUIPMENTENTER\':[],\'QUALITYACCEPT\':{\'itemAccept\':[],\'lotAccept\':[]},\'SECURITYACCEPT\':[],\'OTHER\':[{\'changed\':1,\'content\':\'\',\'attaIds\':\'\',\'enter\':0}],\'SGENVIRONMENT\':[{\'changed\':1,\'content\':\'\',\'attaIds\':\'\',\'enter\':0}]}','lastreviewuser':{'reviewUserId':'13a96f628ec946149aeb87052f2b2c28','roleId':null,'other':1},'dailyFlag':false}"})
    # print(type(dd))
    jso = {'r': 1, 'd': {'same': True}, 'm': '操作成功', 'h': False}
    for i in range(4):
        cc = cc.replace(str(i), jso["m"])
    print(cc)
    # print(json.loads(json.dumps(jso)))
    # print(type(ee))
    # print(type(dataDict.data_dict(ee)),dataDict.data_dict(ee))


    # a = {}
    # b = {'1': '1', '2': '2', '3': {'4': '4', '5': '5'}}
    # c = {'6': '6', '7': {'8': '#'}}
    #
    # for bk, bv in b.items():
    #     if isinstance(bv, dict):
    #         for bbk, bbv in bv.items():
    #             if bbk == '5':
    #                 a['8'] = bv['5']
    # print(a)
    # for ck, cv in c.items():
    #     if isinstance(cv, dict):
    #         for cck, ccv in cv.items():
    #             if cck == '8' and ccv == '#':
    #                 cv['8'] = a['8']
    # print(c)
    #
    # d = {"diary":{"id":"","operate":"#"}}
    # for dk, dv in d.items():
    #     if isinstance(dv, dict):
    #         for ddk, bbdv in dv.items():
    #             if ddk == 'operate':
    #                 dv['operate']=a['8']
    # print(d)
    # getResponseValueID='1,2,3,4'
    # for ResponseValueID in getResponseValueID.split(','):
    #     list(ResponseValueID)

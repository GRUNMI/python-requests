import requests
# from dsy.common.logger import Log
from .configLog import Log

class ConfigHttp:
    mylogger = Log().get_logger()

    def base_url(self, host="http://dsyjg.10333.com"):
        base_url = {"host": host, "timeout": 20}
        return base_url

    def join_url(self, url=''):
        host = self.base_url().get("host")
        url = "".join([host, url])
        return url

    def __get(self, url, params, **kwargs):
        try:
            response = requests.get(url, params, **kwargs)
            if response.status_code == 200 or response.status_code == 302:
                # self.mylogger.info({"request_code": 200, "message": {
                #                    "请求URL：%s" % url, "当前URL：%s" % response.url}})
                # session = requests.session()
                return response
            else:
                result = {
                    "request_code": response.status_code,
                    "message": "请求URL：%s" %
                    url}
        except Exception as e:
            result = {"request": "请求参数错误：%s" % url, "message": e}
        self.mylogger.error(result)

    def __post(self, url, data=None, json=None, **kwargs):
        try:
            response = requests.post(url, data, json, **kwargs)
            if response.status_code == 200:
                self.mylogger.info({"request_code": 200, "message": {
                                   "请求URL：%s" % response.url, "当前URL：%s" % response.url}})
                # session = requests.session()
                return response
            else:
                result = {
                    "request_code": response.status_code,
                    "message": "请求URL：%s" %
                    url}
        except Exception as e:
            result = {"request": "请求参数错误：%s" % url, "message": e}
        self.mylogger.error(result)

    def send_request(self, method, url, params=None, data=None, json=None, **kwargs):
        if method == "get" or method == "GET":
            result = self.__get(url=url, params=params, **kwargs)
        elif method == "post" or method == "POST":
            result = self.__post(url=url, data=data, json=json, **kwargs)
        else:
            result = self.mylogger.error("请求方法有误：%s" % method)
        return result


if __name__ == '__main__':
    request = ConfigHttp()
    url = request.join_url(url="/ent/index")
    r = request.send_request("get", url, verify=False)
    print(r.reason)

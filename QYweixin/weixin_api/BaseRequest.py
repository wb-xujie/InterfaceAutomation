# coding = utf-8
# author = duang

import requests


class Base_class:

    # 将token放入session中
    def __init__(self):
        self.session = requests.Session()
        self.token = self.get_token()
        self.session.params = {"access_token": self.token}

    # 获取token信息
    def get_token(self):
        params = {
            "corpid": "ww1f4a3b6250a35483",
            "corpsecret": "fPQO_LnwS7aZpZpFDqHhGdZgyTdcsWZ6H_8sP-JqATc"
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url, params=params)
        return r.json()["access_token"]

    # 封装请求API
    def send(self, *args, **kwargs):
        return self.session.request(*args, **kwargs)

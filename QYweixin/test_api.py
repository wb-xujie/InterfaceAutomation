# coding = utf-8
# author = duang

import requests

class TestQYweixin:

    # 获取token信息
    def setup(self):
        corpid ="ww1f4a3b6250a35483"
        corpsecret = "fPQO_LnwS7aZpZpFDqHhGdZgyTdcsWZ6H_8sP-JqATc"
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
        self.token = r.json()["access_token"]
        print(self.token)

    # 新增成员
    def test_create_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": "test1111",
            "name": "test1",
            "mobile": "+86 15023491111",
            "department": [1]
        }
        r = requests.post(url,json=data)
        print(r.json())
        # 通过返回的状态码进行断言
        assert r.json()["errcode"] == 0

    # 删除成员
    def test_delte_member(self):
        userID = "test1111"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userID}"
        r = requests.get(url)
        print(r.json())
        assert r.json()["errcode"]==0

    # 更新成员信息
    def test_update_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "test1111",
            "name": "test1111",
        }
        r = requests.post(url,json=data)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 获取成员信息
    def test_get_member(self):
        userID = "test1111"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userID}"
        r = requests.get(url)
        print(r.json())
        assert r.json()["errcode"] == 0
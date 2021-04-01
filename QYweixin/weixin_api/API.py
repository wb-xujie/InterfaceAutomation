# coding = utf-8
# author = duang

from QYweixin.weixin_api.BaseRequest import Base_class


class Address_api(Base_class):
    # 查询成员信息接口
    def get_information(self, userID: str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"
        params = {
            "userid": userID
        }
        r = self.send("GET", url, params=params)
        return r.json()

    # 创建成员接口
    def create_member(self, data: dict):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        # data = {
        #     "userid": "test1111",
        #     "name": "黄忠",
        #     "mobile": "+86 15023491111",
        #     "department": [1]
        # }
        r = self.send("POST", url, json=data)
        return r.json()

    # 删除成员接口
    def delet_member(self, userID: str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params = {"userID": userID}
        r = self.send("GET", url, params=params)
        return r.json()

    # 更新成员信息接口
    def update_information(self, data: dict):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        # data = {
        #     "userid": "test1111",
        #     "name": "test1111",
        # }
        r = self.send("POST", url, json=data)
        return r.json()

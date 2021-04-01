# coding = utf-8
# author = duang
from QYweixin.weixin_api.API import Address_api


class TestAddress:

    # 用例执行前，实例化address页面接口对象
    def setup(self):
        self.address = Address_api()
        self.userID = "test1111"

    def teardown(self):
        pass

    # 查询成员信息接口测试用例
    def test_get_infor(self):
        r = self.address.get_information(self.userID)
        print(r)
        assert r["errcode"] == 0

    # 新增成员接口测试用例
    def test_create(self):
        data = {
            "userid": "test1111",
            "name": "黄忠",
            "mobile": "+86 15023491111",
            "department": [1]
        }
        r = self.address.create_member(data)
        print(r)
        assert r["errcode"] == 0

    # 删除成员接口测试用例
    def test_delet(self):
        r = self.address.delet_member(self.userID)
        print(r)
        assert r["errcode"] == 0

    # 更新成员信息接口测试用例
    def test_update(self):

        data = {
            "userid": "test1111",
            "name": "test1111"
        }
        r = self.address.update_information(data)
        print(r)
        assert r["errcode"] == 0

#
#
# def Alter_batch(data):
#     pass
#
#
# if __name__ == '__main__':
#     data =
import json
import logging
import time
from logging.handlers import RotatingFileHandler
import mitmproxy.http


class MitmEvent:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.url:
            data = self.Alter_data(json.loads(flow.response.text))
            flow.response.text = json.dumps(data)



    def Alter_data(self, data):
        """
        遍历data下面的数据：
        1、如果是字典，继续遍历，递归调用
        2、如果是列表，则遍历列表里面的所有元素
        3、批量修改pecent和current的数据，current*2;percent+10
        
        # """
        if isinstance(data, dict):
            #  如果是dict 就继续遍历 对应的value
            # data.items方法是将字典转换成（key,value）的形式
            for key, value in data.items():
                # 判断是否查找到了股价对应的字典
                if data.get("current")==None:
                    data[key] = self.Alter_data(value)
                else:
                    data['current']= data['current']*2
                    data['percent']=data['percent']+10
                    print(data['current'])
                    break
        # elif isinstance(data, datetime):
        #     data = data
        elif isinstance(data, list):
            # 递归算法，如果是list 就继续遍历列表中的元素
            for item in data:
                self.Alter_data(item)
            # 把 原本的遍历操作使用列表推导式表达出来
            # data = [self.Alter_data(item) for item in data]
        else:
            # 如果是其他数据类型，保持原样
            data = data
        return data

addons = [
    MitmEvent()
]

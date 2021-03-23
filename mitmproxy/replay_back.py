import mitmproxy.http
from mitmproxy import http


class MitmEvent:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        # 拿到请求的url
        url = flow.request.pretty_url
        # 拿到请求的方法
        method = flow.request.method
        # 读取模板文件并转换成字符串
        with open("./demo.txt", 'r', encoding="utf-8") as f:
            data = f.read()
            # 生成自动测试脚本，写入test.py文件
            with open("test.py", 'w', encoding="utf-8") as f:
                f.write(data.format(method=method, url=url))

    def response(self, flow: mitmproxy.http.HTTPFlow):
        pass


addons = [
    MitmEvent()
]

import json

import mitmproxy.http
from mitmproxy import http


class MitmEvent:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.url:
            with open("D:\\Programs\\InterfaceAutomation\\mitmproxy\\quote_xueqiu.json",'r',encoding="utf-8") as f:
                data =f.read()
            flow.response = http.HTTPResponse.make(
                    200,  # (optional) status code
                    data,  # (optional) content
                    {"Content-Type": "text/html"}  # (optional) headers
            )


    def response(self, flow: mitmproxy.http.HTTPFlow):
        pass


addons = [
    MitmEvent()
]
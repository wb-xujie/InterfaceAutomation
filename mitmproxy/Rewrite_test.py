import json

import mitmproxy.http


class MitmEvent:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.url:
            data = json.loads(flow.response.text)
            data['data']['items'][0]['quote']['name'] = "test10000"
            data['data']['items'][0]['quote']['percent'] = "0"

            flow.response.text = json.dumps(data)


addons = [
    MitmEvent()
]
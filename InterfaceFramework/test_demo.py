import requests

class TestDemo:

    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.text)
        print(r.content)
        print(r.url)
        print(r.status_code)
        assert r.status_code == 200


    def test_quary(self):
        parms = {
            'username': 'test',
            'password': "123456"
        }
        r = requests.get('http://httpbin.testing-studio.com/get',params=parms)
        print(r.text)
        assert r.status_code == 200


    def test_form(self):
        form = {
            'username': 'test',
            'password': "123456"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', data = form)
        print(r.text)
        assert r.status_code == 200

    def test_file(self):
        file = {'file':open('D:\Programs\InterfaceAutomation\mitmproxy\demo.txt','rb')}
        r = requests.post('http://httpbin.testing-studio.com/post', files = file)
        print(r.text)
        assert r.status_code == 200

    def test_json(self):
        form = {
            'username': 'test',
            'password': '123'
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=form)
        print(r.text)
        print(r.json()['data']['username'])
        assert r.status_code == 200



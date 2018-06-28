import requests
import json


class YunPian:
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile):
        params = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': '【暮雪Shop】您的验证码是{code}。如非本人操作，请忽略本短信。'.format(code=code)
        }

        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)
        print(re_dict)


if __name__ == '__main__':
    yun_pian = YunPian('8702f295c3bc64f11448c684bbfdd196')
    yun_pian.send_sms('2017', '15542203979')

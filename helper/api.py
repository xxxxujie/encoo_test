import base64
import json
import time
import uuid

import jsonpath
import requests

from common.db import DataBase
from config.setting import Config


class APICase:
    map = {}

    def get_captcha(self):
        """提取验证码"""
        uid = str(uuid.uuid4())
        param = {'uuid': uid}
        url = Config.admin_host + '/captcha.jpg'
        result = requests.request('get', url, params=param)
        return result.content

    def get_code(self, img, uname=None, pwd=None, typeid=3):
        """识别验证码"""
        if uname is None:
            uname = Config.tujian_uname
        if pwd is None:
            pwd = Config.tujian_passwd
        base64_data = base64.b64encode(img)
        b64 = base64_data.decode()
        data = {"username": uname, "password": pwd, "typeid": typeid, "image": img}
        result = json.loads(requests.post("http://api.ttshitu.com/predict"))
        if result['success']:
            return result["data"]["result"]
        else:
            return result["message"]
        return ""

    def admin_login(self, username=None, passwd=None):
        """管理员登录"""
        if username is None:
            username = Config.admin_username
        if passwd is None:
            passwd = Config.admin_passwd
        url = Config.admin_host + '/adminLogin'
        data = {"principal": username, "credentials": passwd, "imageCode": 1}
        response = requests.request('post', url, json=data).json()
        return response['access_token']

    def upload_img(self, token, file_path):
        """上传图片"""
        url = Config.admin_host + '/admin/file/upload/img'
        headers = {"Authorization": f"bearer{token}"}
        f = open(file_path, 'rb')
        file = {"file": f}
        result = requests.request('post', url=url, headers=headers, files=file)
        f.close()
        return result.text

    def get_sms_code(self, mobile):
        """获取手机验证码"""
        url = Config.front_host + 'user/sendRegisterSms'
        data = {"mobile": mobile}
        requests.request('put', url=url, json=data)
        time.sleep(1)
        db = DataBase(**Config.db)
        sql = ""
        validCode = db.query_one(sql)['mobile_code']
        db.close()
        return validCode

    def check_register_sms(self, mobile, validCode):
        """发送手机验证码"""
        url = Config.front_host + 'user/sendRegisterSms'
        data = {"mobile": mobile, "validCode": validCode}
        response = requests.request('put', url=url, json=data)
        return response.text

    def login(self, username=None, passwd=None):
        """登录接口"""
        login_data = {"principal": username, "crendentials": passwd, "appType": 1}
        response = requests.request('post', url=Config.front_host + '/login', json=login_data).json()
        return response['access_token']

    def get_product(self, id):
        """获取商品"""
        params = {"prodId": id}
        url = Config.front_host + '/prod/prodInfo'
        response = requests.request("get", url=url, params=params).json()
        # SKUID
        skuId = jsonpath.jsonpath(response, '$..skuId')[0]
        return skuId

    def api_flow(self, item, map):
        """"""
        # 第一步：数据预处理
        method = item['method']
        url: str = item['url']
        # 如果url用http开头，就不拼接；如果没有，就拼接host
        if not url.startswith('http'):
            url = Config.front_host + url
        # json
        json_data = item['json']
        # 先用replace_data 把数据替换进来，然后再去转成字典
        # map = {"flag":"abc","mobile":"18132349095"}
        # TODO:动态数据替换
        json_data = self.replace_data(json_data, map)
        json_data = json.loads(json_data)
        headers = item.get('headers', None)
        if headers is not None:
            headers = self.replace_data(headers, map)
            headers = json.loads(headers)
        data = item.get('data', None)
        if data is not None:
            data = self.replace_data(data, map)
            data = json.loads(data)

        # 发送请求
        response = self.send_http(method, url=url, json=json_data, headers=headers, data=data)
        return response

    def extract_data(self,item,response):
        """数据提取"""
        if item.get('extract_data','{}'):
            extractor_data = json.loads(item['extract_data'])
            for prop,jspath in extractor_data.items():
                value = jsonpath.jsonpath(response,jspath)[0]
                self.__class__.map[prop] = value
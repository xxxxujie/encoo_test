import json
import unittest

import jsonpath
import requests
from unittestreport import ddt, list_data
from common.excel import read_excel_dict
from config.setting import Config
from helper.api import APICase

# 读取excel
# fspath = r'C:\Users\xujie\PycharmProjects\unittest_RobotAPI\data\cases.xlsx'
items = read_excel_dict(Config.case_file, sheet_name='Sheet1')


@ddt
class TestAdminLogin(unittest.TestCase,APICase):
    def setUp(self) -> None:
        self.map = {}

    @list_data(items)
    def test_01_admin_login(self, item):
        """
        1、准备数据（url、请求方法、请求体、请求头）
        2、数据预处理（处理数据格式）
        3、发送请求（填充测试数据）
        4、断言
        :param item:
        :return:
        """
        # 反序列化：将json转化成字典
        data = item['data']
        # 替换excel中的值
        data = data.repalce('${flag}',self.flag)  # 示例演示
        data = json.loads(data)
        response = self.api_flow(item,self.map)
        print(response)
        self.extract_data(item,response)

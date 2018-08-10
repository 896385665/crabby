# 导入单元测试的类
import unittest
from flask import json

from day04.celltest.demo2 import app


# 自定义类继承于 unittest.TestCase
class LoginTest(unittest.TestCase):
    def setUp(self):
        """初始化，在所有的测试开始之后会调用 setUp方法，这个方法里面可以做：开启测试模式的操作，做测试配置的操作"""
        # 表示当前正在测试，开启测试模式
        app.testing = True
        app.testing = True

    def tearDown(self):
        """在所有的测试函数被执行之后会调用，可以在这里面做一些数据清理操作"""
        pass

    # 测试用户名和密码某一个为空的时候是否返回正确
    def test_none_u_p(self):
        resp = app.test_client().post('/login', data={})
        resp_dict = json.loads(resp.data)
        # 1.断言参数不为空
        self.assertIsNotNone(resp_dict, '返回数据为空')
        # 2.断言字典有errcode
        self.assertIn('errcode', resp_dict, '返回数据中没有errcode')
        # 3.断言errcode = -2
        errcode = resp_dict.get('errcode')
        self.assertEqual(errcode, -2, 'errcode不等于-2')
        print(resp_dict)

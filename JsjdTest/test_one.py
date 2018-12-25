# -*- coding:utf-8 -*-

import unittest       #导入unittest
import requests     #导入requests库
import json            #导入json

class LianXi(unittest.TestCase):              #定义一个类，类的首字母要大写哦
       def setUp(self):                                 #初始化
             self.base_url = 'http://192.168.1.42/'

       def test_get_success(self):             #定义一个方法，切记要以test开头哦
             datalist = {'用户名': 'yujian', '密码': 'Bkc123456'}               #定义传参数据
             head = {"Content-Type": "application/Json"}     #定义头部
             cookies=dict(cookies='')
             r = requests.post(self.base_url, params=datalist, headers=head,cookies=)  # 传入参数
             # result = json.loads(r.text)            使用json格式返回
             print  r.status_code
             print r.base_url
             self.assertEqual(r['status'], 200)      #检验返回值

if __name__ == '__main__':
      unittest.main()



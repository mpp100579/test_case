# -*- coding:utf-8 -*-

'''
import flask
from flask import request
from flask import jsonify
import tools
import OP_db
import settings


# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)


# server.config['JSON_AS_ASCII'] = False

# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route('/login', methods=['get'])
def login():
    # 获取通过url请求传参的数据
    username = request.values.get('name')
    # 获取url请求传的密码，明文
    pwd = request.values.get('pwd')
    # 判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
    if username and pwd:
        # 获取加密后的密码
        password = tools.md5_pwd(pwd)
        # 执行sql，如果查询的username和password不为空，说明数据库存在admin的账号
        sql = 'select name,password from test where name= "%s" and password= "%s";' % (username, password)
        # 从数据查询结果后，res返回是元组
        res = OP_db.getconn(
            host=settings.mysql_info['host'],
            user=settings.mysql_info['user'],
            passwd=settings.mysql_info['pwd'],
            db=settings.mysql_info['db'],
            port=settings.mysql_info['port'],
            sql=sql
        )
        if res:  # res的结果不为空，说明找到了username=admin的用户，且password为加密前的123456
            resu = {'code': 200, 'message': '登录成功'}
            return jsonify(resu)  # 将字典转换为json串, json是字符串
        else:
            resu = {'code': -1, 'message': '账号/密码错误'}
            return jsonify(resu)
    else:
        res = {'code': 999, 'message': '必填参数未填写'}
        return jsonify(res)


if __name__ == '__main__':
    server.run(debug=True, port=8888, host=127.0.0.1)
 # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问







# coding:utf-8

import json
from urlparse import parse_qs
from wsgiref.simple_server import make_server


# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'text/html')])
    # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get
    # 获取当前get请求的所有数据，返回是string类型
    params = parse_qs(environ['QUERY_STRING'])
    # 获取get中key为name的值
    name = params.get('name', [''])[0]
    no = params.get('no', [''])[0]

    # 组成一个数组，数组中只有一个字典
    dic = {'name': name, 'no': no}

    return [json.dumps(dic)]


if __name__ == "__main__":
    port = 5088
    httpd = make_server("0.0.0.0", port, application)
    print "serving http on port {0}...".format(str(port))
    httpd.serve_forever()









'''
# coding:utf-8

import json
from wsgiref.simple_server import make_server


# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'application/json')])
    # environ是当前请求的所有数据，包括Header和URL，body

    request_body = environ["wsgi.input"].read(int(environ.get("CONTENT_LENGTH", 0)))
    request_body = json.loads(request_body)

    name = request_body["name"]
    no = request_body["no"]

    # input your method here
    # for instance:
    # 增删改查

    dic = {'myNameIs': name, 'myNoIs': no}

    return [json.dumps(dic)]


if __name__ == "__main__":
    port = 6088
    httpd = make_server("0.0.0.0", port, application)
    print "serving http on port {0}...".format(str(port))
    httpd.serve_forever()

# -*- coding:utf-8 -*-
import jenkins
url = 'http://192.168.1.220:8080'
username = 'mpp'
password = 'mpp100579'

# 实例化jenkins对象
server = jenkins.Jenkins(url, username, password)

job_name = "mpp_xdj_one"
# 构建项目
print server.build_job(job_name)

# 获取项目相关信息
print server.get_job_info(job_name)

# 获取项目最后次构建号
build_number = server.get_job_info(job_name)['lastBuild']['number']
print build_number

# 获取下一项目构建号
next_build_number = server.get_job_info(job_name)['nextBuildNumber']
print next_build_number

# 某次构建的执行结果状态
print server.get_build_info(job_name, build_number)['result']

# 是否构建中
print server.get_build_info(job_name, build_number)['building']
# 构建项目



import jenkins
url = 'http://192.168.1.220:8080'
username = 'mpp'
password = 'mpp100579'

job_name = "www.linuxhub.org"

# 实例化jenkins对象
server = jenkins.Jenkins(url, username, password)

# 获取下一项目构建号
next_build_number = server.get_job_info(job_name)['nextBuildNumber']

# 构建项目
output = server.build_job(job_name)

# 定时10秒
import time
time.sleep(10)

build_info = server.get_build_info(job_name, next_build_number)

status = build_info['result']

if status == "SUCCESS":
    print "构建成功：%s | 构建项目编号：%s" % (job_name, next_build_number)
else:
    print "构建出错: %s" % job_name
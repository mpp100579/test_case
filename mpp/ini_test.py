# -*- coding:utf-8 -*-

import ConfigParser

config = ConfigParser.ConfigParser()          #生成config对象
config.readfp(open('update.ini'))           #读取打开的update.ini配置文件,

a = config.get("ZIP","MD5")                #获取[ZIP]章节中键是'MD5的值',sections:配置文件中【】中的值
print a  #把[ZIP]章节的键值打印出来
sections = config.sections()  # 获取所有sections[]
print "---update.ini文件中的section内容有：", sections



import ConfigParser

config = ConfigParser.ConfigParser()

# set a number of parameters
config.add_section("book")         #新增章节book
config.set("book", "title", "the python standard library")#新增book章节下的title键值
config.set("book", "author", "fredrik lundh")           #新增book章节下的author下的键值

config.add_section("ematter")
config.set("ematter", "pages", 250)

# write to file
config.write(open('1.ini', "w"))        #写进打开的1.ini配置文件里
sections = config.sections()  # 获取所有sections[]
print "---1.ini文件中的section内容有：", sections


class ConfigFile:
    def __init__(self,iniFile,config):
        self.iniFile=iniFile
        self.config=config
    def ConfigParserSet(self):
        config=ConfigParser.ConfigParser()
        return config
    def readInitFile(self):
        r=config.read(self.iniFile)
        sections = config.sections()  # 获取所有sections
        print "---conf.ini文件中的sections章节内容有：", sections
        # 获取每行数据的键即指定section的所有option，读取所有键用config.options(section章节)
        print "---[zip]章节的所有键为：", config.options("ZIP")

c1=ConfigFile('update.ini',config)
c1.readInitFile()



'''
Created on 2018.6.22
ini配置文件读写的使用by mpp

import ConfigParser

iniFileUrl = "conf.ini"
conf = ConfigParser.ConfigParser()  # 生成conf对象
conf.read(iniFileUrl)  # 读取ini配置文件


def readConfigFile():
    """
    sections:配置文件中[]中的值
    options:每组中的键
    items:键-值的列表形式
    """
    # 获取每组类型中的section值
    sections = conf.sections()  # 获取所有sections
    print "---conf.ini文件中的section内容有：", sections

    # 获取每行数据的键即指定section的所有option，读取所有键用config.options(section章节)
    print "---group_a的所有键为：", conf.options("group_a")
    print "---group_b的所有键为：", conf.options("group_b")

    # 获取指定section的所有键值对             用config.items（section章节）
    print "---group_a的所有键-值为：", conf.items("group_a")

    # 指定section，option读取对应的具体值,读取用config.get（'章节section','键option'）
    print "---group_a组的a_key1值为：", conf.get("group_a", "a_key1")
    print "---group_b组的b_key1值为(取整数类型)：", conf.getint("group_b", "b_key1")


def writeConfigFile():
    """
    根据分组名、键名修改为新键值
    @param sections: section分组名
    @param key: 分组中的key
    @param newvalue: 需要修改后的键值
    """
    #写或者更新用config.set
    conf.set("group_b", "b_key3", "new3")  # 指定section和option则更新value
    conf.set("group_b", "b_key5", "value5")  # 指定section，则增加option和value

   #添加section章节用config.add_section
    conf.add_section("group_d")  # 添加section组
    conf.set("group_d", "d_key1", "value1")  # 给添加的section组增加option-value

    # 写回配置文件
    conf.write(open(iniFileUrl, "wb"))


readConfigFile()
writeConfigFile()
'''
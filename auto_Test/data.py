# coding=utf-8
import json
import xlrd
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def tableToJson():
    source = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\InterfaceData.xlsx")
    table = source.sheet_by_index(0)
    list = []  # 字典列表
    totalList = []  # json列表
    for i in xrange(1, 2):  # 获取第i个表第2行起的值作为用例的参数
        keys = table.col_values(1)  # 获取第i个表第2列的值
        keys.pop(0)
        for j in xrange(3, table.ncols):
            test_value = table.col_values(j)  # 获取第i个表第4列起的值作为用例的参数值
            test_value.pop(0)
            for k in range(len(test_value)):
                s = test_value[k]
                # print s
            data = dict(zip(keys, test_value))  # 等长两列表转为字典
            list.append(data)

    data = {}
    data[table.name] = list
    list = []
    data_to_json = json.dumps(data, ensure_ascii=False, encoding="gb2312")  # 将列表中的unicode转中文
    print u"用例数据：", data_to_json
    totalList.append(data_to_json)

    return totalList


if __name__ == '__main__':
    jsonData = tableToJson()

    # 写入文件
    f = open(r"E:\TestData0618.json", 'w+')
    for i in jsonData:
        f.write(i)
        f.write('\n')
    f.close()
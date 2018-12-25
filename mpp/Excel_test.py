# -*- coding:utf-8 -*-

import xlwt  # excel write
import xlrd
from datetime import date,datetime


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'D:\demo.xlsx')
    # 获取所有sheet
    print workbook.sheet_names()  # [u'sheet1', u'sheet2']
    sheet2_name = workbook.sheet_names()[1]

    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(1)  # sheet索引从0开始
    sheet2 = workbook.sheet_by_name('sheet2')

    # sheet的名称，行数，列数
    print sheet2.name, sheet2.nrows, sheet2.ncols

    # 获取整行和整列的值（数组）
    rows = sheet2.row_values(3)  # 获取第四行内容
    cols = sheet2.col_values(2)  # 获取第三列内容
    print rows
    print cols

    # 获取单元格内容
    print sheet2.cell(1, 0).value.encode('utf-8')
    print sheet2.cell_value(1, 0).encode('utf-8')
    print sheet2.row(1)[0].value.encode('utf-8')

    # 获取单元格内容的数据类型
    print sheet2.cell(2, 2).ctype   #因为获取单元格的日期格式不能直接获取，需要查询获取这个日期1990/2/22返回的数据类型，而ctype类型代表 :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    print sheet2.cell(1,1).ctype
    print sheet2.cell(2,2).value       #获取当前单元格的值
    date_value =xlrd.xldate_as_tuple(sheet2.cell_value(2, 2), workbook.datemode)
    print date_value
    print date(*date_value[:3]).strftime('%Y/%m/%d') #使用xlrd的xldate_as_tuple来处理为date格式，先判断表格的ctype=3时xldate才能开始操作


if __name__ == '__main__':
    read_excel()

# 创建一个Workbook对象，这就相当于创建了一个Excel文件
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
'''
Workbook类初始化时有encoding和style_compression参数
encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。
默认是ascii。当然要记得在文件头部添加：
#!/usr/bin/env python
# -*- coding: utf-8 -*-
style_compression:表示是否压缩，不常用。
'''
# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
# 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表
sheet = book.add_sheet('test', cell_overwrite_ok=True)
# 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False
# 向表test中添加数据
sheet.write(0, 0, 'EnglishName')  # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
sheet.write(1, 0, 'Marcovaldo')
txt1 = '中文名字'
sheet.write(0, 1, txt1.decode('utf-8'))  # 此处需要将中文字符串解码成unicode码，否则会报错
txt2 = '马可瓦多'
sheet.write(1, 1, txt2.decode('utf-8'))

# 最后，将以上操作保存到指定的Excel文件中
book.save(r'e:\test1.xls')  # 在字符串前加r，声明为raw字符串，这样就不会处理其中的转义了。否则，


#读取excel文件
xlsfile = r"C:\Users\Administrator\Desktop\test\Account.xls"# 打开指定路径中的xls文件
book = xlrd.open_workbook(xlsfile)#得到Excel文件的book对象，实例化对象
sheet0 = book.sheet_by_index(0) # 通过sheet索引获得sheet对象
print "1、",sheet0
sheet_name = book.sheet_names()[0]# 获得指定索引的sheet表名字
print "2、",sheet_name
sheet1 = book.sheet_by_name(sheet_name)# 通过sheet名字来获取，当然如果知道sheet名字就可以直接指定
nrows = sheet0.nrows    # 获取行总数
print "3、",nrows
#循环打印每一行的内容
for i in range(nrows):
    print sheet1.row_values(i)
ncols = sheet0.ncols    #获取列总数
print "4、",ncols
row_data = sheet0.row_values(0)     # 获得第1行的数据列表
print row_data
col_data = sheet0.col_values(0)     # 获得第1列的数据列表
print "5、",col_data
# 通过坐标读取表格中的数据
cell_value1 = sheet0.cell_value(0, 0)
print "6、",cell_value1
cell_value2 = sheet0.cell_value(0, 1)
print "7、",cell_value2

'''

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height

    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6

    style.font = font
    # style.borders = borders
    return style
# 写excel
def write_excel():
    f = xlwt.Workbook()  # 创建工作簿

    
    #创建第一个sheet:
      #sheet1
   
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
    column0 = [u'机票', u'船票', u'火车票', u'汽车票', u'其它']
    status = [u'预订', u'出票', u'退票', u'业务小计']

    # 生成第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))

    # 生成第一列和最后一列(合并4行)
    i, j = 1, 0
    while i < 4 * len(column0) and j < len(column0):
        sheet1.write_merge(i, i + 3, 0, 0, column0[j], set_style('Arial', 220, True))  # 第一列
        sheet1.write_merge(i, i + 3, 7, 7)  # 最后一列"合计"
        i += 4
        j += 1

    sheet1.write_merge(21, 21, 0, 1, u'合计', set_style('Times New Roman', 220, True))
    # 生成第二列
    i = 0
    while i < 4 * len(column0):
        for j in range(0, len(status)):
            sheet1.write(j + i + 1, 1, status[j])
        i += 4
    f.save('TEST_excel1.xlsx')  # 保存文件

if __name__ == '__main__':
    # generate_workbook()
    # read_excel()
    write_excel()





#创建第二个sheet:sheet2
def write_excel():
    f = xlwt.Workbook()  # 创建工作簿

    sheet2 = f.add_sheet(u'sheet2',cell_overwrite_ok=True) #创建sheet2
    row0 = [u'姓名',u'年龄',u'出生日期',u'爱好',u'关系']
    column0 = [u'小杰',u'小胖',u'小明',u'大神',u'大仙',u'小敏',u'无名']
#生成第一行
    for i in range(0,len(row0)):
        sheet2.write(0,i,row0[i],set_style('Times New Roman',220,True))
#生成第一列
    for i in range(0,len(column0)):
        sheet2.write(i+1,0,column0[i],set_style('Times New Roman',220))

    sheet2.write(1,2,'1991/11/11')
    sheet2.write_merge(7,7,2,4,u'暂无') #合并列单元格
    sheet2.write_merge(1,2,4,4,u'好朋友') #合并行单元格

    f.save(u'test_sheet2.xlsx') #保存文件
'''
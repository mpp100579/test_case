from calculate.sc_cal import *            #从包下的py模块文件引入py文件的方法
__all__ = ['A','func']#__all__=[]用列表形式把方法暴露给别人调用，在别的模块中，导入该模块时，只能导入__all__中的变量，方法和类
#是一个字符串list，用来定义模块中对于from XXX import *时要对外导出的符号，即要暴露的借口，但它只对import *起作用，对from XXX import XXX不起作用。
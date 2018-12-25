# coding=utf-8
class MPP:
    def __init__(self, name,age):
        self._name = name
        self._age=age

    def loveMpp(self):
        print ("I love YOU {0}:{1}".format(self._name , self._age))
class WZX(MPP):
    def _init_(self):
        MPP._init_(self,name,age)

    def loveWZX(self):
        print("I love YOU {0}:{1}".format(self._name ,self._age))

m = MPP("闵盼盼","27岁")
m.loveMpp()

W = WZX("吴振兴","31岁")
W.loveWZX()

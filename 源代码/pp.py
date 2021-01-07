# coding=utf-8
from Widget import *


class PP(Widget):#选择修改哪一个权限
    def __init__(self,ppp):
        super(PP, self).__init__(300, 60, "选择")
        self.ppp = ppp
        self.btn1 = Btn(self.root,'准假权限',10,10,80,40,self.change1)
        self.btn2 = Btn(self.root,'取消',110,10,80,40,self.change0)
        self.btn3 = Btn(self.root,'销假权限',210,10,80,40,self.change2)

    def change1(self):#选择准假权限
        self.ppp[0] = 1
        self.close()

    def change0(self):#选择取消
        self.ppp[0] = 0
        self.close()

    def change2(self):#选择销假权限
        self.ppp[0] = 2
        self.close()


if __name__ == '__main__':
    test = PP()
    test.start()

# coding=utf-8
from Widget import *
import Data
import pp


def getp(p):
    if p == 0:
        return '无权限'
    else:
        return '有权限'


class Admin(Widget):#管理员界面
    def __init__(self):#初始化界面
        super(Admin, self).__init__(630, 420, "老师")
        self.table = Table(self.root, 10, 10, 610, 400, 3, ['老师', '准假','销假'])
        self.table.setWidths([200, 200])#设置宽度
        self.table.setDbClick(self.dbclick)#设置双击信号
        self.initData()#初始化数据
        self.pp = [0]#回执数据

    def dbclick(self,*args):#双击
        try:
            self.ppp = [0]
            self.hide()
            p = pp.PP(self.ppp)
            p.setCloseCallback(self.changed)
            p.start()
        except:
            pass
    def changed(self):#根据选择更改数据
        self.show()
        for item in self.table.selection():
            tes = self.table.item(item, 'values')
            print(tes,self.ppp)
            if self.ppp[0] == 1:
                if tes[1] == '无权限':
                    Data.adminP1(tes[0], 1)
                else:
                    Data.adminP1(tes[0], 0)
            else:
                if tes[2] == '无权限':
                    Data.adminP2(tes[0], 1)
                else:
                    Data.adminP2(tes[0], 0)
            self.initData()
            return

    def initData(self):#初始化数据
        self.table.clear()
        ds = Data.admin()
        try:
            for s in ds:
                self.table.add([s[1], getp(s[5]), getp(s[6])])
        except:
            pass


if __name__ == '__main__':
    test = Admin()
    test.start()

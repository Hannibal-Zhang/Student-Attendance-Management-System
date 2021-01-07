# coding=utf-8
from Widget import *
import Work
import Data
import Session


class Teacher(Widget):#老师界面
    def __init__(self):
        super(Teacher, self).__init__(1030, 400, "老师")
        self.table = Table(self.root, 10, 10, 1010, 350, 5, [ '姓名','学号','班级','课程', '状态'])
        self.table.setWidths([200, 200, 200, 200, 200])
        nameLab = Lab(self.root,'姓名:',10,360,50)
        self.name = Text(self.root,70,360,100)
        sidLab = Lab(self.root,'学号:',180,360,50)
        self.sid = Text(self.root,240,360,160)
        self.btn = Btn(self.root, '查询', 410, 360, 100, 40, self.query)
        self.btn = Btn(self.root, '查看考勤表', 520, 360, 100, 40, self.work)
        self.table.setDbClick(self.dbclick)
        self.initData()

    def query(self):
        name = self.name.get()
        sid = self.sid.get()
        self.table.clear()
        ds = Data.tea()
        try:
            for s in ds:
                if name != '' and s[1] != name:
                    continue
                if sid != '' and s[0] != sid:
                    continue
                self.table.add([s[1], s[0],s[6],s[7], Work.getState(s[4])])
        except:
            pass

    def dbclick(self,*args):#双击，查询是否可更改并更改
        for item in self.table.selection():
            tes = self.table.item(item,'values')
            print(tes[4])
            if tes[4] == '申请请假':
                if Session.session.p1() != 1:
                    messagebox.showerror('错误','没有准假权限')
                    return
                Data.teaP1(tes[1])
                self.initData()
            return

    def work(self):#打开考勤表
        self.hide()
        work = Work.Work()
        work.setCloseCallback(self.calls)
        work.start()

    def calls(self):#修改考勤表后更新数据
        self.show()
        self.initData()

    def initData(self):#初始化数据
        self.table.clear()
        ds = Data.tea()
        try:
            for s in ds:
                self.table.add([s[1],s[0],s[6],s[7], Work.getState(s[4])])
        except:
            pass


if __name__ == '__main__':
    test = Teacher()
    test.start()

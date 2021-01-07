# coding=utf-8
from Widget import *
import Work
import Data
from Session import session


class Student(Widget):#学生界面
    def __init__(self,uid):
        super(Student, self).__init__(300, 100, "学生")

        self.uid = session.uid()
        self.sid = session.sid()
        self.name = session.name()

        self.apply = Btn(self.root, "请假", 10, 30, 80, 40, lambda : self.do(0))
        self.come = Btn(self.root, "签到", 110, 30, 80, 40, lambda : self.do(1))
        self.query = Btn(self.root, "查询", 210, 30, 80, 40, self.work)

        # print(Data.stuApply(uid))
        # print(Data.stuCome(uid))
        if Data.stuApply(uid) is not None or Data.stuCome(uid)[4] != -1:
            self.apply.setEnable(False)
            self.come.setEnable(False)


    def do(self,state):#请假或者签到，0请假，1签到
        Data.stu(self.sid,self.name,state,self.uid)
        self.apply.setEnable(False)
        self.come.setEnable(False)

    def work(self):#查看考勤记录
        self.hide()
        work = Work.Work(self.uid)
        work.setCloseCallback(self.show)
        work.start()


if __name__ == '__main__':
    test = Student()
    test.start()

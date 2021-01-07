# coding=utf-8
from Session import session
from sys import exit as quit
import Login,Student,Data,Teacher,Admin
import _thread

if __name__ == '__main__':#程序入口

    login = Login.Login()#首先登录，登录成功再根据登录角色进入不同子系统
    login.start()

    Data.initNow()#初始化每日首次数据

    if session.uid() is None:#登录失败，退出程序
        quit()
    elif session.role() == 0:#学生
        stu = Student.Student(session.uid())
        stu.start()
    elif session.role() == 1:#老师
        teacher = Teacher.Teacher()
        teacher.start()
    elif session.role() == 2:#管理员
        admin = Admin.Admin()
        admin.start()
    quit()
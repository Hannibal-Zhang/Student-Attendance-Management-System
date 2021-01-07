# coding=utf-8
from Widget import *
import Data


class Register(Widget):#注册界面
    def __init__(self):
        super(Register, self).__init__(500, 650, "注册")
        self.uid = Text(self.root, 175, 110, 275)
        self.pwd = Text(self.root, 175, 160, 275)
        self.name = Text(self.root, 175, 210, 275)
        self.sid = Text(self.root, 175, 260, 275)
        self.sex = Text(self.root, 175, 310, 275)
        self.scl = Text(self.root, 175, 360, 275)
        self.cou = Text(self.root, 175, 410, 275)
        self.zy = Text(self.root, 175, 460, 275)
        self.cla = Text(self.root, 175, 510, 275)

        self.register = Btn(self.root, "注册", 175, 600, 150, 40, self.password)
        btns = [['学生',75,560,100,40],['老师',325,560,100,40]]
        self.btns = Radios(self.root,btns)
        self.btns.setClick(self.radioClick)

    def radioClick(self,*args):
        if self.btns.get() == 0:
            self.sidLab.setText('学号:')
            self.zyLab.show()
            self.claLab.show()
            self.zy.show()
            self.cla.show()
        else:
            self.sidLab.setText('工号:')
            self.zyLab.hide()
            self.claLab.hide()
            self.zy.hide()
            self.cla.hide()

    def initUI(self):#初始化提示ui
        title = Lab(self.root, "注册", 0, 0, 500, 50)
        title.setFont(("黑体", 36))
        uidLab = Lab(self.root, '用户名:', 50, 110, 100)
        pwdLab = Lab(self.root, "登录密码:", 50, 160, 100)
        nameLab = Lab(self.root, '姓名:', 50, 210, 100)
        self.sidLab = Lab(self.root, "学号:", 50, 260, 100)
        sexLab = Lab(self.root, '性别:', 50, 310, 100)
        sclLab = Lab(self.root, "学院:", 50, 360, 100)
        couLab = Lab(self.root, "课程:", 50, 410, 100)
        self.zyLab = Lab(self.root, '专业:', 50, 460, 100)
        self.claLab = Lab(self.root, "班级:", 50, 510, 100)

        # imgLab = Lab(self.root, '', 10, 10, 100, 100)
        # imgLab.setAutoImg("/images/work.jpg")

    def password(self):#注册验证
        uid = self.uid.getText()
        pwd = self.pwd.getText()
        name = self.name.getText()
        sid = self.sid.getText()
        sex = self.sex.getText()
        scl = self.scl.getText()
        zy = self.zy.getText()
        cla = self.cla.getText()
        cou = self.cou.getText()
        if Data.register(uid, pwd,name,sid,self.btns.get(),sex,scl,zy,cla,cou):
            self.close()
        else:#注册返回false，代表用户名已经有了
            messagebox.showerror(title="注册错误", message='用户名重复或者其他错误.')


if __name__ == '__main__':
    login = Register()
    login.start()
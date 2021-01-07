# coding=utf-8
from Widget import *
import Data
import Register


class Login(Widget):#登录界面
    def __init__(self):
        super(Login, self).__init__(500, 350, "登录")
        self.uid = Text(self.root, 175, 130, 275)
        self.pwd = Text(self.root, 175, 230, 275)
        self.login = Btn(self.root, "登录", 50, 300, 150, 40, self.password)
        self.register = Btn(self.root, "注册", 300, 300, 150, 40, self.register)

    def initUI(self):#初始化提示ui
        title = Lab(self.root, "登录", 0, 0, 500, 50)
        title.setFont(("黑体", 36))
        uidLab = Lab(self.root, '用户名:', 50, 130, 100)
        pwdLab = Lab(self.root, "登录密码:", 50, 230, 100)

        imgLab = Lab(self.root, '', 10, 10, 100, 100)
        imgLab.setAutoImg("images/work.jpg")

    def password(self):#登录验证
        uid = self.uid.getText()
        pwd = self.pwd.getText()
        if Data.login(uid,pwd):
            self.close()
        else:
            messagebox.showerror(title="登录错误",message='用户名或密码错误.')

    def register(self):#打开注册界面
        self.hide()
        register = Register.Register()
        register.setCloseCallback(self.show)
        register.start()


if __name__ == '__main__':
    #test = Login()
    print(os.path.split(os.path.abspath(__file__))[0])

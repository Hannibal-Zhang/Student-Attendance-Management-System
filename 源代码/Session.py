# coding=utf-8
class Session:#会话状态保存
    def __init__(self):
        super(Session, self).__init__()
        self.session = {'uid': None, 'role': None,'name':None,'sid':None,'course':None, 'power': {'p1': 0, 'p2': 0},'class':None}
        #保存当前登录用户的信息

    def set(self, uid, role,name,sid, cla, cou, power=None):
        self.session['uid'] = uid
        self.session['role'] = int(role)
        self.session['name'] = name
        self.session['sid'] = sid
        self.session['class'] = cla
        self.session['course'] = cou
        if power is not None:
            self.session['power'] = {'p1': int(power[0]), 'p2': int(power[1])}

    def cou(self):
        return self.session['course']

    def cla(self):
        return self.session['class']

    def uid(self):
        return self.session['uid']

    def role(self):
        return self.session['role']

    def name(self):
        return self.session['name']

    def sid(self):
        return self.session['sid']

    def p1(self):
        return self.session['power']['p1']

    def p2(self):
        return self.session['power']['p2']

    def print(self):
        print(self.session['uid'])
        print(self.session['role'])
        print(self.session['power']['p1'])
        print(self.session['power']['p2'])


session = Session()

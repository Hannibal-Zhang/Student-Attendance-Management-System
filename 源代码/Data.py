# coding=utf-8
from Sql import *
from Session import session
import time


def ts():#得到当前时间戳
    return int(round(time.time() * 1000))


def now(full=False):#返回当前时间
    if full:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return time.strftime("%Y-%m-%d", time.localtime())


def initNow():#初始化每日的数据，在每日首次运行系统时，添加所有学生的未到记录
    sql = Sql()
    d = sql.get('now')
    if d is None:
        sql.insert('now',[[now()]])
    elif d[0] == now():
        return
    else:
        sql.update('now',{'date':now()})
    ss = sql.select('user','*',{'role':0})
    if ss is not None:
        for s in ss:
            u = sql.get('work','*',{'sid':s[0],'date':now()})
            # print(u)
            if u is None:
                sql.insert('work',[[s[0],s[1],now(),s[2],-1,ts(),s[10],s[11]]])

def login(uid, pwd):#验证登录
    if uid == 'admin' and pwd == 'admin':
        session.set('admin', 2,'管理员','admin','','')
        return True
    data = Sql().get('user', whe={'uid': uid, 'pwd': pwd})
    if data is None:
        return False
    else:
        session.set(data[2],data[4],data[1],data[0],data[10],data[11],[data[5],data[6]])
        return True


def register(uid, pwd,name,sid, role,sex,sch,zy,cla,cou):#验证注册数据并通过
    if uid == 'admin' and pwd == 'admin':
        session.set('管理员', 2)
    sql = Sql()
    if sql.get('user', whe={'uid': uid}) is not None:
        return False
    sql.insert('user', [[sid,name,uid, pwd, role, 1, 0,sex,sch,zy,cla,cou]])
    if role == 0:
        sql.insert('work',[[sid,name,now(),uid,-1,ts(),cla,cou]])
    return True


def Work(uid=None):#从数据库查询考勤记录并以时间戳排序
    if uid is None:
        return Sql().select('work', order=' order by ts')
    else:
        return Sql().select('work', '*', {'uid': uid}, ' order by ts')


def stuApply(uid):#获取学生今天请假申请
    return Sql().get('apply', whe={'uid': uid, 'date': now()})


def stuCome(uid):#获取学生今天签到
    return Sql().get('work', whe={'uid': uid, 'date': now()})


def stu(sid,name,state, uid):#改变学生的考勤状态
    if state == 0:
        Sql().insert('apply', [[sid, name, now(), uid]])
    else:
        Sql().delete('apply', {'date': now(), 'uid': uid})
        Sql().update('work', {'state': 0}, {'date': now(), 'uid': uid})


def tea():#老师获取所有的考勤记录，并且用申请请假覆盖未到状态
    sql = Sql()
    tes = sql.select('work', whe={'date': now()})
    for i in range(0,len(tes)):
        if sql.get('apply',whe={'date':tes[i][2],'uid':tes[i][3]})is not None:
            tes[i] = list(tes[i])
            tes[i][4] = -2
    return tes


def teaP1(sid):#老师准假，删除申请，更新请假状态
    sql = Sql()
    sql.delete('apply', {'date': now(), 'sid': sid})
    sql.update('work', {'state': 1}, {'date': now(), 'sid': sid})


def teaP2(date, sid):#老师销假，更新请假为签到状态
    Sql().update('work', {'state': 0}, {'date': date, 'sid': sid})

def admin():#管理员获取所有老师信息
    return Sql().select('user',whe={'role':1})

def adminP1(uid,p1):#管理员修改老师准假权限
    Sql().update('user',{'p1':p1},{'name':uid})

def adminP2(uid,p2):#管理员修改老师销假权限
    Sql().update('user',{'p2':p2},{'name':uid})
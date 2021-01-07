# coding=utf-8
from Widget import *
import Data
from tkinter import filedialog
import xlwt
from Session import session


def getState(state):#根据数字返回考勤状态文字描述
    if state == 0:
        return '签到'
    elif state == 1:
        return '请假'
    elif state == -2:
        return '申请请假'
    else:
        return '未到'


class Work(Widget):#考勤界面
    def __init__(self,uid=None):
        super(Work, self).__init__(1230, 400, "考勤表")
        self.uid = uid
        self.table = Table(self.root,10,10,1210,350,6,['日期','学生姓名','学生学号','班级','课程','状态'])
        self.table.setWidths([200,200,200,200,200,200])
        self.initData()
        if self.uid is None:#根据打开角色，来放置数据和是否导出
            dateLab = Lab(self.root,'日期筛选:',170,360,70)
            self.date = Text(self.root,240,360,200)
            self.btn = Btn(self.root,'导出',450,360,130,40,self.out)
            self.table.setDbClick(self.dbclick)
            claLab = Lab(self.root,'班级筛选:',600,360,70)
            self.cla = Text(self.root,670,360,200)

    def dbclick(self,*args):#双击查询是否可更改
        for item in self.table.selection():
            tes = self.table.item(item,'values')
            if tes[5] == '请假':
                if session.p2() != 1:
                    messagebox.showerror('错误', '没有销假权限')
                    return
                Data.teaP2(tes[0],tes[2])
                self.initData()
            return

    def initData(self):#初始化数据
        self.table.clear()
        self.ds = Data.Work(self.uid)
        if self.ds is not None:
            for d in self.ds:
                self.table.add([d[2],d[1],d[0],d[6],d[7],getState(d[4])])

    def out(self):#导出到xlsx
        path = filedialog.asksaveasfilename(title='选择导出文件',initialdir='./',defaultextension='xlsx',filetypes=[('*.xlsx','xlsx'),('*.xls','xls')])
        if path != '':
            file = xlwt.Workbook()
            table = file.add_sheet('学生考勤状态',cell_overwrite_ok=True)
            table.write(0, 0, '日期')
            table.write(0, 1, '姓名')
            table.write(0, 2, '学号')
            table.write(0, 3, '班级')
            table.write(0, 4, '课程')
            table.write(0, 5, '状态')
            date = self.date.get()
            cla = self.cla.get()
            con = 1
            for i in range(0,len(self.ds)):
                if (self.ds[i][2] != date and date != '') or (self.ds[i][6] != cla and cla != ''):
                    continue
                table.write(con, 0, self.ds[i][2])
                table.write(con, 1, self.ds[i][1])
                table.write(con, 2, self.ds[i][0])
                table.write(con, 3, self.ds[i][6])
                table.write(con, 4, self.ds[i][7])
                table.write(con, 5, getState(self.ds[i][4]))
                con += 1
            file.save(path)
            messagebox.showinfo('提示','导出成功')



if __name__ == '__main__':
    test = Work()
    test.start()

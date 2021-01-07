# coding=utf-8

from tkinter import Tk, GROOVE, StringVar, IntVar
from tkinter.ttk import Button, Label, Entry, Treeview, Radiobutton
from tkinter import messagebox
from PIL import Image, ImageTk
#import os


# __init__(self,w=1000,h=500,title='系统',x=None,y=None):
class Widget:#常用ui控件封装，Button, Label, Entry, Treeview, Radiobutton
    def __init__(self, w=1000, h=500, title='系统', x=None, y=None):
        self.root = Tk()
        if x is None:
            self.resize(w, h)
        else:
            self.setGeometry(x, y, w, h)
        self.root.title(title)
        self.initUI()
        self.closeCallback = None

    def close(self):#关闭
        self.root.destroy()
        if self.closeCallback is not None:
            self.closeCallback()

    def setCloseCallback(self, func):#设置关闭回执函数
        self.closeCallback = func
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.close() if func() is None else self.close())

    def __del__(self):
        pass

    def hide(self):#隐藏
        self.root.withdraw()

    def show(self):#显示
        self.root.update()
        self.root.deiconify()

    def start(self):#开始消息循环
        self.root.mainloop()

    def initUI(self):
        pass

    def setTitle(self, title):#设置标题
        self.root.title(title)

    def resize(self, w, h):#设置大小
        self.width = w
        self.height = h
        self.root.geometry(str(w) + 'x' + str(h))

    def setGeometry(self, x, y, w, h):#设置大小位置
        self.width = w
        self.height = h
        self.root.geometry(str(w) + 'x' + str(h) + '+' + str(x) + "+" + str(y))

    def move(self, x, y):#设置位置
        self.root.geometry(str(self.width) + 'x' + str(self.height) + '+' + str(x) + "+" + str(y))


class uiModel:
    width = 0
    height = 0

    def move(self, x, y):
        if x is not None:
            self.place(x=x)
        elif y is not None:
            self.place(y=y)

    def resize(self, w, h):
        if w is not None:
            self.width = w
            self.place(width=w)
        if h is not None:
            self.height = h
            self.place(height=h)

    def setGeometry(self, x = -1, y = -1, w = -1, h = -1):
        if x == -1:
            self.place(x=self.x, y=self.y, width=self.width, height=self.height)
            return
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.place(x=x, y=y, width=w, height=h)

    def setText(self, text):#设置显示文字
        self.configure(text=text)

    def setFont(self, font=("黑体", 12)):#设置字体
        self.configure(font=font)

    def hide(self):
        self.place_forget()

    def show(self):
        self.setGeometry()

    def setClick(self, func, mouse=1,isPrint=False):#设置单击信号
        if isPrint:
            print('setClick')
        self.bind('<Double-Button-' + str(mouse) + '>', func)

    def setDbClick(self, func, mouse=1):#设置双击信号
        self.bind('<Double-Button-' + str(mouse) + '>', func)

    def setEnable(self, state):#设置是否不可操作
        if state:
            self.configure(state='normal')
        else:
            self.configure(state='disabled')


# __init__(self,root,text='Button',x=0,y=0,w=100,h=40,command=None):
class Btn(Button, uiModel):
    def __init__(self, root, text='Button', x=0, y=0, w=100, h=40, command=None):
        super(Btn, self).__init__(root, text=text, command=command)
        self.setGeometry(x, y, w, h)


# __init__(self,root,text=None,x=0,y=40,w=100,h=40):
class Lab(Label, uiModel):
    def __init__(self, root, text='', x=0, y=40, w=100, h=40):
        super(Lab, self).__init__(root, text=text, img=None, anchor='center')
        self.setGeometry(x, y, w, h)

    def setImg(self, path=None):#设置显示图片
        if path == None:
            self.configure(image=None)
            self.img = None
            return
        import os
        pil_image = Image.open(os.path.abspath(os.path.dirname(__file__)) + path)
        pil_image = pil_image.resize((self.width, self.height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(pil_image)
        self.configure(image=img)
        self.img = img

    def setAutoImg(self, path):#设置自适应图片
        pil_image = Image.open(path)
        w = pil_image.size[0]
        h = pil_image.size[1]
        if w / self.width < h / self.height:
            w = int(w * (self.height / h))
            h = self.height
        else:
            h = int(h * (self.width / w))
            w = self.width
        pil_image = pil_image.resize((w, h), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(pil_image)
        self.configure(image=img)
        self.img = img


# __init__(self,root,x=0,y=80,w=100,h=40,text=None):
class Text(Entry, uiModel):
    def __init__(self, root, x=0, y=80, w=100, h=40, text=None):
        if text is not None:
            self.setText(text)
        super(Text, self).__init__(root)
        self.setGeometry(x, y, w, h)

    def setText(self, text):
        self.set(text)

    def getText(self):
        return self.get()


# __init__(self,root,x=0,y=120,w=100,h=80,columns=2,headText=['1','2']):
class Table(Treeview, uiModel):
    def __init__(self, root, x=0, y=120, w=100, h=80, columns=2, headText=['1', '2']):
        self.col = columns
        cs = []
        for i in range(0, columns):
            cs.append(str(i + 1))
        super(Table, self).__init__(root, show='headings', columns=cs)
        for i in range(0, columns):
            self.column(str(i + 1), anchor='center')
            self.setHeadText(i, headText[i])
        self.setGeometry(x, y, w, h)

    def setHeadText(self, col, text):#设置标题
        self.heading(str(col + 1), text=text)

    def setHeadTexts(self, texts):#设置多标题
        for i in range(0, len(texts)):
            self.setHeadText(i, texts[i])

    def setWidth(self, col, width):#设置宽度
        self.column(str(col + 1), width=width)

    def setWidths(self, widths):#设置多宽度
        for i in range(0, len(widths)):
            self.setWidth(i, widths[i])

    def add(self,data,index=None):#添加数据
        self.insert('','end' if index is None else index,values=data)

    def getData(self):#获取选中数据
        for item in self.selection():
            item_text = self.item(item, "values")
            data = []
            for i in range(0, self.col):
                data.append(item_text[i])
            return data

    def clear(self):#清空
        cs = self.get_children()
        [self.delete(item) for item in cs]


# __init__(self, root, val, value, text, x=0, y=80, w=100, h=40):
class Radio(Radiobutton, uiModel):
    def __init__(self, root, val, value, text, x=0, y=80, w=50, h=30):
        self.click = None
        super(Radio, self).__init__(root, text=text, command=lambda : self.__clicked(val,value), value=value)
        self.setGeometry(x, y, w, h)

    def __clicked(self,val,value):
        val.set(value)
        if self.click is not None:
            self.click()

    def setClick(self,func):
        self.click = func


# __init__(self, root, btns):
class Radios():
    def __init__(self, root, btns):
        self.__val = IntVar()
        self.__btns = []
        # self
        for i in range(0,len(btns)):
            btn = Radio(root, self.__val, i, btns[i][0])
            btn.setGeometry(btns[i][1], btns[i][2], btns[i][3], btns[i][4])
            self.__btns.append(btn)

    def  get(self):
        return self.__val.get()

    def btn(self,con):
        if con >= len(self.__btns):
            return None
        else:
            return self.__btns[con]

    def setClick(self,func):
        for i in range(0,len(self.__btns)):
            self.__btns[i].setClick(func)


if __name__ == '__main__':
    test = Widget()
    test.start()

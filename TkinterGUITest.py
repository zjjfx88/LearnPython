# -*- coding:utf-8 -*-
# 第一步是导入Tkinter包的所有内容：
from Tkinter import *
import tkMessageBox

# 第二步是从Frame派生一个Application类，这是所有Widget的父容器：
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createInput()

    def createWidgets(self):
        self.helloLabel = Label(self,text='Hello, World')
        self.helloLabel.pack()
        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()

    def createInput(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self,text='Hello',command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()

#设置窗口标题
app.master.title('Hello world')

# 主消息循环
app.mainloop()
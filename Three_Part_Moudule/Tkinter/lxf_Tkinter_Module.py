# python支持多种图形界面的第三方库包括, Tk, wxWidgets, Qt, GTK
# python自带的库是支持Tk的Tkinter
# Tk是一个图形库, 支持多个操作系统使用Tcl语言开发;
# Tk会调用操作系统提供的本地GUI接口, 完成最终的GUI
# 
# example
from tkinter import *
# 从Frame派生一个Application类, 这是所有Widget的父容器
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack() # 把Widget加入到父容器中, 并实现布局
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self, text='Hello, world!')
		self.helloLabel.pack()
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()
# 再GUI中, 每个Button, Label, 输入框都是一个Widget, Frame
# 是容纳其他Wedget的Widget, 所有Widget组合起来就是一颗树
# 
# pack()方法把Widget加入到父容器中, 并实现布局, 
# pack()是最简单的布局, grid()可以实现更复杂的布局

# 实例化Application, 并启动消息循环
app = Application()
# 设置窗口标题
app.master.title('Hello')
# 主消息循环:
app.mainloop()

# 输入文本
from tkinter import *
import tkinter.messagebox as messagebox

class Application1(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self, text='Hello', command=self.hello)
		self.alertButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application1()
app.master.title('Hello, world!')
app.mainloop()
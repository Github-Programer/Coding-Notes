#coding:UTF-8
#ch9.py fill
from tkinter import *

root = Tk()
root.title("普通设置控件")

Label(root, text="Tkinter", bg="lightyellow").pack(fill=X)
#第一个标签
#这些标签不需要保存在变量中，设置好直接布局
Label(root, text="wxPython", bg="lightgreen").pack()

Label(root, text="PyQt", bg="lightblue").pack(fill=X)

root.mainloop()
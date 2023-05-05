import subprocess
from tkinter import *

def execute_program():
    # 从键盘上的输入也在窗口内完成并将程序的输出显示在窗口内
    # 这里只是一个示例，你需要将你的程序放在这里
    process = subprocess.Popen(['python', 'C:\Users\ziyuemu\Desktop\python与深度学习基础\lab01pythonblogtoword.py'], stdout=subprocess.PIPE)
    output_label.config(text="Hello World!")

top = Tk() #创建窗口
top.title("新浪博客特定作者文章下载") #定义窗口名称
top.geometry('500x300') #设置主窗口大小，注意中间对的符号是小写字母x

#创建文本标签Label,top是第一个参数为父窗口，text是标签内容
#设置位置参数，使用place方法可将控件放在指定位置，
#place()方法中窗口显示区左上角是(0,0),x是向右递增，y是向下递增
output_label = Label(top,text = "点击开始执行")
output_label.place(x = 200,y = 100)

#创建按钮，text是功能按钮的名称
Button(top,text = "开始执行程序", command=execute_program).place(x = 220,y = 150)

top.mainloop()





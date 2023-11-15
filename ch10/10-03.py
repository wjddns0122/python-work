from tkinter import *
window = Tk()

lable1 = Label(window, text = "COOKBOOK~~ Python을")
lable2 = Label(window, text= "열심히", font=("궁서체", 30), fg="blue")
lable3 = Label(window, text="공부 중 입니다.", bg= "magenta", width=20, height=5, anchor=SE)

lable1.pack()
lable2.pack()
lable3.pack()

window.mainloop()
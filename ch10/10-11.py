from tkinter import *

## 전역 변수 사용 부분 ##
btnList = [None] * 9
fnameList = ["gif/froyo.gif", "gif/gingerbread.gif", "gif/honeycomb.gif", "gif/icecream.gif",
             "gif/jellybean.gif", "gif/kitkat.gif", "gif/lollipop.gif", "gif/marshmallow.gif", "gif/nougat.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("210x210")

for i in range(0, 9):
    photoList[i] = PhotoImage(file = fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()
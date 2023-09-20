import turtle as myT
import random

## 함수 선언 부분 ##
def screenLeftClick(x,y):
    global r,g,b
    myT.pencolor(r,g,b)
    myT.pendown()
    myT.goto(x,y)

def screenRightClick(x,y):
    myT.penup()
    myT.goto(x,y)

def screenMidClick(x,y):
    global r,g,b
    tSize = random.randrange(1,10)
    myT.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
myT.title('거북이로 그림 그리기')
myT.shape('turtle')
myT.pensize(pSize)

myT.onscreenclick(screenLeftClick, 1)
myT.onscreenclick(screenMidClick, 2)
myT.onscreenclick(screenRightClick, 3)

myT.done()
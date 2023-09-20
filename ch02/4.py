import turtle 
import random

## 함수 선언 부분 ##
def screenLeftClick(x,y):
    global r,g,b
    turtle.pendown()
    turtle.goto(x,y)
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor(r,g,b)
## 터틀 그래픽 프로그램을 수정해서 마우스 왼쪽 버튼과 마우스 가운데 버튼의 기능을 통합. 마우스 왼쪽 버튼만 눌러도 임의의 색상이 지정되고 거북이의 크기가 변경되면서 선이 그려지도록 ##
def screenRightClick(x,y):
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick(x,y):
    global r,g,b
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
import turtle ## 터틀 모듈 불러오기 ##
import random ## 랜덤 모듈 불러오기 ##

## 함수 선언 부분 ##
def screenLeftClick(x,y):   ## 왼쪽 화면을 클릭할떄 선언되는 함수
    global r,g,b            ## 전역 변수
    turtle.pendown()        ## 그리기
    turtle.goto(x,y)        ## 이동
    tSize = random.randrange(1, 10)    ## 1부터 9까지 랜덤
    turtle.shapesize(tSize)     ## 거북이 크기
    r = random.random()     ## r, g, b 랜덤 받기
    g = random.random()
    b = random.random()
    turtle.color(r,g,b)     ## 색상 받기

    turtle.stamp()          ## 거북이 스탬프 찍기

## 변수 선언 부분 ##
pSize = 10
r, g, b = 0, 0, 0

## 메인 코드 부분 ##
turtle.title('거북이 도장 찍기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)

turtle.done()
import turtle
import random
import math
from tkinter.simpledialog import askstring

swidth, sheight = 500, 500
radius, txtSize = 20, 20

turtle.title('거북이 나선형 글자쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)
turtle.speed(0)
turtle.penup()

inStr = askstring('문자열 입력', '거북이로 쓸 문자열을 입력')
angle = 45  # 회전 각도

for ch in inStr:
    tX = radius * math.cos(math.radians(angle))
    tY = radius * math.sin(math.radians(angle))
    
    r = random.random()
    g = random.random()
    b = random.random()

    turtle.goto(tX, tY)
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))
    
    radius -= 10  
    angle -= 15   

turtle.done()

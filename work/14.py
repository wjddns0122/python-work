import turtle
import random

# 전역 변수 설정
min_side_length = 10
max_side_length = 200
colors = ["red", "green", "blue", "orange", "purple", "pink"]

# 메인 코드
turtle.speed(0)
turtle.bgcolor("white")
turtle.title('거북이가 랜덤한 별 그리기')

while True:
    side_length = random.randint(min_side_length, max_side_length)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    color = random.choice(colors)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)

    for i in range(5):
        turtle.forward(side_length)
        turtle.right(144)

    turtle.clear()

turtle.done()

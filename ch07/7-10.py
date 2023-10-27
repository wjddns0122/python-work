import turtle
import random

# 거북이 리스트 생성
turtle_list = []

# 스크린 설정
screen = turtle.Screen()
screen.title("거북이 리스트 활용 (정렬)")
screen.bgcolor("white")

# 거북이 생성 및 랜덤 위치와 크기 설정
for _ in range(5):
    t = turtle.Turtle()
    t.penup()
    t.speed(1)
    t.shape("turtle")
    t.color(random.random(), random.random(), random.random())  # 랜덤 색상
    t.goto(random.uniform(-200, 200), random.uniform(-200, 200))
    t.shapesize(random.randrange(1, 100) / 10)
    turtle_list.append(t)

# 스탬프 찍고 선 그리기
for i in range(len(turtle_list) - 1):
    t1 = turtle_list[i]
    t2 = turtle_list[i + 1]
    t1.stamp()
    t1.setheading(t1.towards(t2))
    t1.pendown()
    t1.goto(t2.xcor(), t2.ycor())

turtle.done()

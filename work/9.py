import turtle
import random

def screenLeftClick(x, y):
    tSize = random.randint(1, 10)
    r, g, b = random.random(), random.random(), random.random()

    turtle.pendown()
    turtle.color(r, g, b)
    turtle.goto(x, y)
    turtle.shapesize(tSize)
    turtle.stamp()

def main():
    turtle.title('거북이 도장 찍기')
    turtle.shape('turtle')
    turtle.pensize(10)

    turtle.onscreenclick(screenLeftClick, 1)

    turtle.done()

if __name__ == "__main__":
    main()
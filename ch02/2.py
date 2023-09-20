import turtle

MyT = None

MyT = turtle.Turtle()
MyT.shape('turtle')

for i in range(0, 4, +1):
    MyT.forward(200)
    MyT.right(90)

MyT.done()

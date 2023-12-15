## 클래스 선언 부분 ##
class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

    if speed >= 150:
        speed = 150

## 메인 코드 부분 ##
myCar1 = Car()
myCar1.color = "빨강"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "파랑"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 0

myCar4 = Car()
myCar4.color = "초록"
myCar4.speed = 0

myCar1.upSpeed(30)
print("자동차1의 색상은 %s 이며, 현재 속도는 %dKm 입니다." % (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s 이며, 현재 속도는 %dKm 입니다." % (myCar2.color, myCar2.speed))

myCar3.upSpeed(0)
print("자동차3의 색상은 %s 이며, 현재 속도는 %dKm 입니다." % (myCar3.color, myCar3.speed))

myCar4.upSpeed(200)
print("자동차4의 색상은 %s 이며, 현재 속도는 %dKm 입니다." % (myCar4.color, myCar4.speed))
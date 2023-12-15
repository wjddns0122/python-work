class Car:
    def method(self):
        print("슈퍼 클래스")

class Sedan(Car):
    def method(self):
        print("서브 클래스")

myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()
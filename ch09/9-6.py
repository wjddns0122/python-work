## 함수 선언 부분 ##
def func1():
    a = 10          ## 지역 변수
    print("func()1에서 a값 %d" % a)

def func2():
    print("func()2에서 a값 %d" % a)

## 전역 변수 선언 부분 ##
a = 20

## 메인 코드 부분 ##
func1()
func2()
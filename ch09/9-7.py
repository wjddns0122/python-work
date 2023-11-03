## 함수 선언 부분 ##
def func1():
    global a        ## 지역 변수가 아닌 전역 변수로 사용할려면 -> global
    a = 10
    print('func1()에서 a값 %d' % a)

def func2():
    print('func2()에서 a값 %d' % a)

## 전역 변수 선언 부분 ##
a = 20

## 메인 코드 부분 ##
func1()
func2()
import sys

## 변수 선언 부분 ##
intVar, floatVar, boolVar = 0, 0.0, True
strVar, listVar, tupleVar, dictVar, setVar = [None] * 5

## 메인 코드 부분 ##
if __name__ == "__main__":
    intVar = 0
    floatVar = 0.0
    boolVar = True
    strVar = ""
    listVar = []
    tupleVar = ()
    dictVar = {}
    setVar = set()

    print('int형 기본 크기 -->', sys.getsizeof(intVar))
    print('float형 기본 크기 -->', sys.getsizeof(floatVar))
    print('bool형 기본 크기 -->', sys.getsizeof(boolVar))
    print('str형 기본 크기 -->', sys.getsizeof(listVar))
    print('list형 기본 크기 -->', sys.getsizeof(listVar))
    print('tuple형 기본 크기 -->', sys.getsizeof(tupleVar))
    print('dictionary형 기본 크기 -->', sys.getsizeof(dictVar))
    print('set형 기본 크기 -->', sys.getsizeof(setVar)) 
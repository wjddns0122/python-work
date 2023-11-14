## 함수 선언 부분 ##
def calc(v1, v2, op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        if v2 != 0:
            result = v1 / v2
        else:
            print("0으로는 나누면 안 됩니다.ㅠㅠ")
    elif op == '**':
        result = v1 ** v2
    
    return result

## 전역 변수 선언 부분 ##
res = 0
var1, var2, oper = 0, 0, ""

## 메인 코드 부분 ##
var1 = int(input("첫 번쨰 수를 입력하세요 : "))
oper = input("계산을 입력하세요(+,-,*,/,**) : ")
var2 = int(input("두 번째 수를 입력하세요 : "))

res = calc(var1, var2, oper)

print("## 계산기 : %d %s %d = %d" % (var1,oper,var2, res))
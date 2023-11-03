import random
import turtle

def to_binary(num):
    return bin(num)[2:].zfill(8)

def bit_operation(num1, num2, operator):
    if operator == '&':
        result = num1 & num2
    elif operator == '|':
        result = num1 | num2
    elif operator == '^':
        result = num1 ^ num2
    return result

def display_result(result):
    turtle.shape('turtle')
    turtle.clear()
    turtle.penup()
    if result == 1:
        turtle.color("red")
        turtle.shapesize(2)
    else:
        turtle.color("blue")
        turtle.shapesize(1)
    turtle.stamp()

## 메인 함수 부분 ##
def main():
    score = 0
    for _ in range(10):
        operator = random.choice(['&', '|', '^'])
        num1 = random.randint(0, 255)
        num2 = random.randint(0, 255)
        
        binary1 = to_binary(num1)
        binary2 = to_binary(num2)
        
        print("피연산자 1:", binary1)
        print("피연산자 2:", binary2)
        print("연산자:", operator)

        answer = int(input("계산 결과를 입력하세요 (0 또는 1): "))

        result = bit_operation(num1, num2, operator)
        display_result(result)

        if answer == result:
            print("맞았습니다!")
            score += 10
        else:
            print("틀렸습니다!")

        print()

    print("점수:", score)

main()
import turtle

## 전역 변수 선언 부분 ##
swidth, sheight = 1000, 300
curX, curY = 0, 0

## 비트 논리곱 함수 ##
def bitwise_and(bin1, bin2):
    # 두 2진수의 길이를 맞춰줍니다.
    len1, len2 = len(bin1), len(bin2)
    if len1 < len2:
        bin1 = '0' * (len2 - len1) + bin1
    elif len1 > len2:
        bin2 = '0' * (len1 - len2) + bin2

    result = ""
    for i in range(len(bin1)):
        if bin1[i] == '1' and bin2[i] == '1':
            result += '1'
        else:
            result += '0'
    return result

## 메인 코드 부분 ##
if __name__ == "__main__":
    turtle.title('비트 논리곱 구현하기')
    turtle.shape('turtle')
    turtle.setup(width=swidth + 50, height=sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    binary1 = input("첫 번째 2진수를 입력하세요: ")
    binary2 = input("두 번째 2진수를 입력하세요: ")

    # 입력된 2진수와 비트 논리곱 계산
    result_binary = bitwise_and(binary1, binary2)

    curX = swidth / 2
    curY = 0

    for i in range(len(result_binary)):
        turtle.goto(curX, curY)
        if result_binary[i] == '1':
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50

    print("비트 논리곱 결과:", result_binary)

    turtle.done()

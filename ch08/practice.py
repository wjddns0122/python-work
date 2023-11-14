# ss='IT_CookBook'
# print(ss[0])
# print(ss[1:2])
# print(ss[3:])
# print(ss[:4])
# print(ss[0:-1])

# aa = 'Python'
# print(aa[0])
# print(aa[1:2])
# print(aa[-3:-1])
# print(aa[3:])

# str1 = 'Hanbit'
# str2 = 'Network'

# print(str1 + str2)
# print(2 * str1)
# print(str1 * str2)
# print(str1 / str2)
# print(str1 - str2)

# inStr = 'IT_CookBook_Python'
# outStr = ''

# for i in range(0, len(inStr)):
#     if i % 2 == 0:
#         outStr += inStr[i]
#     else:
#         outStr += '#'

# print(outStr)

# str1 = '코딩 중에서 파이썬 코딩이 가장 즐거운 코딩'

# print(str1.count('코딩'))
# print(str1.rfind('코딩'))
# print(str1.startswith('코딩'))
# print(str1.find('파이썬'))

# ss = 'Python 파이썬'
# print(ss.change('파이썬', 'Python'))
# print(ss.replace('파이썬', 'Python'))
#  
# print(ss.replace('Python', '파이썬'))

# inStr, outStr = "Python", ""
# strLen = len(inStr)

# for i in range(0, strLen):
#     outStr += ## 빈칸을 입력하세요
# print("내용을 거꾸로 출력 : %s" % outStr)

# input_str = "파이썬 ### CookBook $$$ @@@ 열공중 1234"
# result_str = ""

# for char in input_str:
#     if char.isalpha():
#         result_str += char

# print("입력된 문자열에서 한글과 영문자만 남깁니다:", result_str)

# input_str = input("문자열을 입력하세요: ")

# uppercase_str = ""
# lowercase_str = ""
# numeric_str = ""
# korean_str = ""
# other_str = ""

# for char in input_str:
#     char_ord = ord(char)
#     if char.isnumeric():
#         numeric_str += char
#     elif char.isalpha():
#         if char.islower():
#             lowercase_str += char
#         elif char.isupper():
#             uppercase_str += char
#     elif 44032 <= char_ord <= 55203:  # Korean character range in Unicode
#         korean_str += char
#     else:
#         other_str += char

# print("대문자:", uppercase_str)
# print("소문자:", lowercase_str)
# print("숫자:", numeric_str)
# print("한글:", korean_str)
# print("기타:", other_str)

import turtle
import random
from tkinter.simpledialog import *
import math

## 전역 변수 선언 부분 ##
inStr = ''
swidth, sheight = 500, 500
tX, tY, txtSize = [0] * 3
radius = 200
angle = 0
num_rotations = 2

## 메인 코드 부분 ##
turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열 입력')

for _ in range(num_rotations):
    for ch in inStr:
        angle_rad = math.radians(angle)
        tX = radius * math.cos(angle_rad)
        tY = radius * math.sin(angle_rad)
        r = random.random(); g = random.random(); b = random.random()
        txtSize = 20

        turtle.goto(tX, tY)
        turtle.setheading(angle)

        turtle.pencolor((r, g, b))
        turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))
        
        angle += 360 / len(inStr)

turtle.done()

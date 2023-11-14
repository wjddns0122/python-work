# def f1():
#     print(var)
#     df = 1
#     return df 

# def f2():
#     var = 10
#     print(var)

# var = 100
# f1()
# f2()


# def addNumber(num):
#     add = 0
#     for i in range(1, num + 1):
#         add += i
#     return add

# print(addNumber(100))

def base2(num):
    if num == 0:
        return ''
    else:
        return base2(num // 2) + str(num % 2)

def base8(num):
    if num == 0:
        return ''
    else:
        return base8(num // 8) + str(num % 8)

def base16(num):
    hex_chars = "0123456789ABCDEF"
    if num == 0:
        return ''
    else:
        return base16(num // 16) + hex_chars[num % 16]

# 메인 코드
decimal_number = int(input("10진수 입력 ---> "))
binary_result = base2(decimal_number)
octal_result = base8(decimal_number)
hexadecimal_result = base16(decimal_number)

print(f"2진수 : {binary_result}, 8진수 : {octal_result}, 16진수 : {hexadecimal_result}")

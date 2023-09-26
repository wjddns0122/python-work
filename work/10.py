a = input("글자 입력 : ")

if all(bit in '01' for bit in a):
    print('2진수 또는 8진수 또는 10진수 또는 16진수입니다.')

elif all(oct_digit in '01234567' for oct_digit in a):
    print('8진수 또는 10진수 또는 16진수입니다.')

elif a.isdigit():
    print('10진수 또는 16진수입니다.')

elif all(hex_digit in '0123456789ABCDEFabcdef' for hex_digit in a):
    print('16진수입니다.')

else:
    print('숫자가 아닙니다')
a = int(input("시프트할 숫자는?"))
b = int(input("출력할 횟수는?"))
result = 0

for b in range(1, b + 1):
    result = a << b
    print("%d << %d = %d" % (a, b, result))

for b in range(1, b + 1):
    result = a >> b
    print("%d >> %d = %d" % (a, b, result))
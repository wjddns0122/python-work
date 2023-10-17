start = int(input("*** 첫 번째 숫자를 입력하세요 : "))
end = int(input("*** 두 번째 숫자를 입력하세요 : "))
step = int(input("*** 더할 숫자를 입력하세요 : "))
total_sum = 0

for number in range(start, end + 1, step):
    total_sum += number

print("%d+%d+...+%d는 %d" % (start, start + step, end, total_sum))
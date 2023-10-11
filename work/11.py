c500 = int(input("500원짜리 개수 --> "))
c100 = int(input("100원짜리 개수 --> "))
c50 = int(input("50원짜리 개수 --> "))
c10 = int(input("10원짜리 개수 --> "))

total = (c500 * 500) + (c100 * 100) + (c50 * 50) + (c10 * 10)
print("## 동전의 합계 ==> {}원".format(total))
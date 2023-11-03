a = int(input("두 자리 숫자의 정수를 입력해 주세요 : "))
b = int(input("세 자리 숫자의 정수를 입력해 주세요 : "))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_add(start, end):
    primes = []
    prime_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
            prime_sum += num
    print("소수 : ", primes)
    print("소수 합 : ", prime_sum )


def fiveandsevenprimeadd(start, end):
    multiples = []
    multiples_sum = 0
    for num in range(start, end + 1):
        if num % 5 == 0 and num % 7 == 0:
            multiples.append(num)
            multiples_sum += num
    print("5의 배수이면서 7의 배수인 수:", multiples)
    print("합:", multiples_sum)

prime_add(min(a,b),max(a,b))
fiveandsevenprimeadd(min(a, b), max(a, b))
import threading
import time

## 클래스 선언 부분 ##
class SumThread:
    def __init__(self, name, limit):
        self.threadName = name
        self.limit = limit
        self.sumResult = 0

    def calculateSum(self):
        for i in range(1, self.limit + 1):
            self.sumResult += i
            time.sleep(0.001)  # 스레드가 너무 빨리 종료되지 않도록 약간의 지연을 추가

    def getSumResult(self):
        return self.sumResult

## 메인 코드 부분 ##
# 각 스레드 객체 생성
thread1 = SumThread('Thread1', 1000)
thread2 = SumThread('Thread2', 100000)
thread3 = SumThread('Thread3', 10000000)

# 각 스레드 시작
th1 = threading.Thread(target=thread1.calculateSum)
th2 = threading.Thread(target=thread2.calculateSum)
th3 = threading.Thread(target=thread3.calculateSum)

th1.start()
th2.start()
th3.start()

# 각 스레드가 종료될 때까지 대기
th1.join()
th2.join()
th3.join()

# 결과 출력
print(f"{thread1.threadName}의 합: {thread1.getSumResult()}")
print(f"{thread2.threadName}의 합: {thread2.getSumResult()}")
print(f"{thread3.threadName}의 합: {thread3.getSumResult()}")

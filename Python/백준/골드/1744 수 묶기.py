from collections import deque


class Main:
    def __init__(self):
        self.n = int(input())
        self.nums = [int(input()) for _ in range(self.n)]
        self.positives = []  # 2 이상의 양수
        self.negatives = []  # 0 및 음수
        self.ones = 0  # 1의 개수
        self.answer = 0

    def separate_num(self):
        for num in self.nums:
            if num > 1:
                self.positives.append(num)
            elif num == 1:
                self.ones += 1
            else:
                self.negatives.append(num)

        self.positives.sort()  # 2 이상의 양수 정렬
        self.negatives.sort(reverse=True)  # 음수 및 0 정렬 -> 값을 뒤에서부터 제거

    @staticmethod
    def calculate(arr):
        total = 0
        while len(arr) > 1:
            a = arr.pop()
            b = arr.pop()
            total += a * b  # 곱하는 것이 더 유리
        if arr:
            total += arr.pop()  # 남은 숫자가 있으면 더하기
        return total

    def solve(self):
        self.separate_num()
        self.answer += self.calculate(self.positives)  # 2 이상의 양수
        self.answer += self.calculate(self.negatives)  # 음수와 0
        self.answer += self.ones  # 1은 묶지 않고 더함
        print(self.answer)


problem = Main()
problem.solve()
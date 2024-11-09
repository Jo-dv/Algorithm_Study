class Main:
    def __init__(self):
        self.n = int(input())
        self.arr = list(map(int, input().split()))
        self.answer = []

    def solve(self):
        dp = [1] * self.n
        prev = [-1] * self.n  # 이전 인덱스 추적을 위한 배열

        max_length = 0
        max_index = 0

        for i in range(1, self.n):  # dp 계산 및 prev 배열 채우기
            for j in range(i):
                if self.arr[i] > self.arr[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j  # 이전 인덱스 기록

            if dp[i] > max_length:  # 최대 길이와 그 위치 업데이트
                max_length = dp[i]
                max_index = i

        while max_index != -1:  # 역추적
            self.answer.append(self.arr[max_index])
            max_index = prev[max_index]

        self.answer.reverse()  # 역추적이므로 리스트를 뒤집어야 올바른 순서가 됨

        print(len(self.answer))
        print(*self.answer)


problem = Main()
problem.solve()

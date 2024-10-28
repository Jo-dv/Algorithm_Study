class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.temperature = list(map(int, input().split()))
        self.answer = -float('inf')

    def solve(self):
        current = sum(self.temperature[:self.k])
        self.answer = max(self.answer, current)
        for i in range(self.k, self.n):  # 주어진 범위가 있고, 데이터들이 연속적이므로 효율적인 계산을 위해 Sliding Window로 해결
            current -= self.temperature[i-self.k]
            current += self.temperature[i]
            self.answer = max(self.answer, current)

        print(self.answer)


problem = Main()
problem.solve()

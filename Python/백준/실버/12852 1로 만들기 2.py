class Main:
    def __init__(self):
        self.n = int(input())
        self.dp = [0] * (self.n + 1)
        self.tracking = [0 for _ in range(self.n + 1)]
        self.answer = []

    def solve(self):
        for i in range(2, self.n + 1):
            self.dp[i] = self.dp[i - 1] + 1
            prev = i - 1
            if i % 3 == 0 and self.dp[i // 3] + 1 < self.dp[i]:
                self.dp[i] = self.dp[i // 3] + 1
                prev = i // 3
            if i % 2 == 0 and self.dp[i // 2] + 1 < self.dp[i]:
                self.dp[i] = self.dp[i // 2] + 1
                prev = i // 2
            self.tracking[i] = prev

        s = self.n
        while True:
            self.answer.append(s)
            if s == 1:
                print(self.dp[self.n])
                print(*self.answer)
                break
            s = self.tracking[s]


problem = Main()
problem.solve()
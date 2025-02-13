class Main:
    def __init__(self):
        self.n = int(input())
        self.answer = 0

    def solve(self):
        dp = [float('inf')] * 100001
        dp[0] = 1
        dp[2] = 1
        dp[4] = 2
        dp[5] = 1

        for i in range(6, self.n + 1):
            dp[i] = min(dp[i - 2], dp[i - 5]) + 1

        print(-1 if dp[self.n] == float('inf') else dp[self.n])


problem = Main()
problem.solve()
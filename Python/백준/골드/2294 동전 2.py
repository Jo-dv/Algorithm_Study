import sys


class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.coins = [int(input()) for i in range(self.n)]

    def solve(self):
        dp = [sys.maxsize] * (self.k + 1)
        dp[0] = 0

        for coin in self.coins:
            for i in range(coin, self.k + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        print(-1 if dp[self.k] == sys.maxsize else dp[self.k])


problem = Main()
problem.solve()
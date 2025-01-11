class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())

    def solve(self):
        dp = [[1] * (self.n + 1) for _ in range(self.k + 1)]

        for i in range(2, self.k + 1):
            for j in range(1, self.n + 1):
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000

        print(dp[self.k][self.n])


problem = Main()
problem.solve()

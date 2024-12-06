class Main:
    def __init__(self):
        self.n = int(input())

    def solve(self):
        dp = [0] * (self.n + 1)

        if self.n > 0:
            dp[1] = 1
            for i in range(2, self.n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]

        print(dp[self.n])


problem = Main()
problem.solve()
class Main:
    def __init__(self):
        self.n = int(input())

    def solve(self):
        dp = [0] * 91
        dp[1] = 1  # 1

        for i in range(2, 91):
            dp[i] = dp[i - 1] + dp[i - 2]

        print(dp[self.n])


problem = Main()
problem.solve()
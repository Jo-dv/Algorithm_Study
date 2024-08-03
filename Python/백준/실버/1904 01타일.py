class Main:
    def __init__(self):
        self.n = int(input())

    def solve(self):
        dp = [0] * 1000001
        dp[1] = 1
        dp[2] = 2

        for i in range(3, 1000001):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

        print(dp[self.n])


problem = Main()
problem.solve()
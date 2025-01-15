class Main:
    def __init__(self):
        self.n = int(input())
        self.nums = [int(input()) for _ in range(self.n)]

    def solve(self):
        dp = [[0 for _ in range(4)] for _ in range(100001)]

        dp[1] = [0, 1, 0, 0]  # 끝이 1로 끝나는 경우
        dp[2] = [0, 0, 1, 0]  # 끝이 2로 나오는 경우
        dp[3] = [0, 1, 1, 1]  # 끝이 1, 2, 3으로 끝나는 경우 각각 존재

        for i in range(4, 100001):
            dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % 1000000009  # 1로 끝날 때는 2와 3인 경우만 고려
            dp[i][2] = (dp[i - 2][3] + dp[i - 2][1]) % 1000000009
            dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % 1000000009

        for num in self.nums:
            print(sum(dp[num]) % 1000000009)


problem = Main()
problem.solve()
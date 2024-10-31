class Main:
    def __init__(self):
        self.n = int(input())
        self.life = list(map(int, input().split()))  # 잃는 체력
        self.joy = list(map(int, input().split()))  # 얻는 기쁨

    def solve(self):
        dp = [0] * 101
        for i in range(self.n):
            for j in range(100, self.life[i] - 1, -1):
                if j - self.life[i] > 0:
                    dp[j] = max(dp[j], dp[j - self.life[i]] + self.joy[i])

        print(dp[-1])


problem = Main()
problem.solve()
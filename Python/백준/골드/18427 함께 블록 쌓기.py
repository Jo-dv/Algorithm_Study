class Main:
    def __init__(self):
        self.n, self.m, self.h = map(int, input().split())
        self.blocks = [list(map(int, input().split())) for _ in range(self.n)]

    def solve(self):
        dp = [0] * (self.h + 1)  # dp[x]: 높이가 x인 탑을 만드는 경우의 수
        dp[0] = 1  # 높이 0을 만드는 경우의 수는 1

        for student_blocks in self.blocks:
            next_dp = dp[:]  # 현재 상태를 복사
            for block in student_blocks:
                for height in range(self.h, block - 1, -1):
                    next_dp[height] = (next_dp[height] + dp[height - block]) % 10007

            dp = next_dp  # 업데이트

        print(dp[self.h])


problem = Main()
problem.solve()

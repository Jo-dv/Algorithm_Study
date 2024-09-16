class Main:
    def __init__(self):
        self.n = int(input())
        self.a = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        dp = [[1] * self.n for _ in range(2)]

        for i in range(1, self.n):
            for j in range(i):
                if self.a[j] < self.a[i]:  # 정방향 증가 수열 탐색
                    dp[0][i] = max(dp[0][i], dp[0][j] + 1)
                if self.a[(self.n - 1) - j] < self.a[(self.n - 1) - i]:  # 역순 증가 수열 탐색 -> 순방향 시점 감소
                    dp[1][(self.n - 1) - i] = max(dp[1][(self.n - 1) - i], dp[1][(self.n - 1) - j] + 1)

        for i in zip(*dp):  # 각 열을 한 번에 처리
            self.answer = max(self.answer, sum(i) - 1)

        print(self.answer)


problem = Main()
problem.solve()
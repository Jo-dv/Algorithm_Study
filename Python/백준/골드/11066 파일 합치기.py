import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.t = int(input())
        self.k = None
        self.files = None

    def solve(self):
        for _ in range(self.t):
            self.k = int(input())
            self.files = list(map(int, input().split()))

            prefix_sum = [0] * (self.k + 1)
            for i in range(1, self.k + 1):
                prefix_sum[i] = prefix_sum[i - 1] + self.files[i - 1]

            dp = [[0] * self.k for _ in range(self.k)]

            for length in range(2, self.k + 1):  # 부분 파일 길이
                for start in range(self.k - length + 1):  # 시작 인덱스
                    end = start + length - 1  # 끝 인덱스
                    dp[start][end] = float('inf')
                    for mid in range(start, end):
                        cost = dp[start][mid] + dp[mid + 1][end] + (prefix_sum[end + 1] - prefix_sum[start])
                        dp[start][end] = min(dp[start][end], cost)

            print(dp[0][self.k - 1])


problem = Main()
problem.solve()
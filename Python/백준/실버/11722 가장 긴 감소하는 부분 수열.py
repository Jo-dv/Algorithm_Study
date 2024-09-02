class Main:
    def __init__(self):
        self.n = int(input())
        self.arr = list(map(int, input().split()))

    def solve(self):
        dp = [1] * self.n

        for i in range(1, self.n):
            for j in range(i):
                if self.arr[j] > self.arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        print(max(dp))


problem = Main()
problem.solve()
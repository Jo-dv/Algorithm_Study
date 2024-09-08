class Main:
    def __init__(self):
        self.n = int(input())
        self.arr = list(map(int, input().split()))

    def solve(self):
        in_dp = [1] * self.n
        de_dp = [1] * self.n

        for i in range(1, self.n):
            if self.arr[i - 1] <= self.arr[i]:
                in_dp[i] = max(in_dp[i], in_dp[i - 1] + 1)
            if self.arr[i - 1] >= self.arr[i]:
                de_dp[i] = max(de_dp[i], de_dp[i - 1] + 1)

        print(max(max(in_dp), max(de_dp)))


problem = Main()
problem.solve()

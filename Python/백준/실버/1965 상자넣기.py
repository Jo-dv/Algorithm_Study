class Main:
    def __init__(self):
        self.n = int(input())
        self.boxes = list(map(int, input().split()))

    def solve(self):
        dp = [1] * self.n

        for i in range(1, self.n):
            for j in range(0, i):
                if self.boxes[j] < self.boxes[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        print(max(dp))


problem = Main()
problem.solve()
class Main:
    def __init__(self):
        self.t = int(input())
        self.test_case = [tuple(map(int, input().split())) for _ in range(self.t)]

    def solve(self):
        max_case = max(self.test_case)[0]
        dp = [0] * (max_case + 1)
        dp[1] = 1

        for i in range(2, max_case + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        for i, data in enumerate(self.test_case, 1):
            p, q = data
            print(f'Case #{i}: {dp[p] % q}')


problem = Main()
problem.solve()

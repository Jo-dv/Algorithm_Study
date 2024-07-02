class Main:
    def __init__(self):
        self.t = int(input())
        self.n = None
        self.coins = None
        self.m = None

    def solve(self):
        for _ in range(self.t):
            self.n = int(input())
            self.coins = list(map(int, input().split()))
            self.m = int(input())
            memo = [0] * (self.m + 1)
            memo[0] = 1  # 무조건 하나는 만들 수 있음
            for coin in self.coins:
                for i in range(coin, self.m+1):
                    memo[i] += memo[i-coin]  # 현재 동전을 뺐을 때 만들 수 있는 동전의 수

            print(memo[self.m])


problem = Main()
problem.solve()
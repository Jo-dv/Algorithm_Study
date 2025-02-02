class Main:
    def __init__(self):
        self.a, self.b = map(int, input().split())
        self.b = min(self.b, 10**7)  # 1천만 이후에는 소수 팰린드롬 없음
        self.prime_check = [True] * (self.b + 1)

    def sieve(self):
        self.prime_check[0] = self.prime_check[1] = False  # 0과 1은 소수 아님
        for i in range(2, int(self.b ** 0.5) + 1):
            if self.prime_check[i]:
                for j in range(i * i, self.b + 1, i):
                    self.prime_check[j] = False

    def solve(self):
        self.sieve()

        for num in range(self.a, self.b + 1):
            if self.prime_check[num] and str(num) == str(num)[::-1]:
                print(num)

        print(-1)


problem = Main()
problem.solve()

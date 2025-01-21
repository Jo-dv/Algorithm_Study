import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.d, self.k, self.c = map(int, input().split())
        self.sushi = [int(input()) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        check = defaultdict(int)
        eat = 0

        for i in range(self.k):
            if check[self.sushi[i]] == 0:
                eat += 1
            check[self.sushi[i]] += 1

        if check[self.c] == 0:
            eat += 1
        check[self.c] += 1

        self.answer = eat
        for i in range(self.n):
            if check[self.sushi[i]] == 1:
                eat -= 1
            check[self.sushi[i]] -= 1

            next_sushi = self.sushi[(i + self.k) % self.n]
            if check[next_sushi] == 0:
                eat += 1
            check[next_sushi] += 1

            self.answer = max(self.answer, eat)

        print(self.answer)


problem = Main()
problem.solve()
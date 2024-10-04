from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.cards = [int(input()) for _ in range(self.n)]

    def solve(self):
        check = defaultdict(int)

        for card in self.cards:
            check[card] += 1

        result = sorted(check.items(), key=lambda x: (-x[1], x[0]))
        print(result[0][0])


problem = Main()
problem.solve()
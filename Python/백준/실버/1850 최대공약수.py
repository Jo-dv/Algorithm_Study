from math import gcd


class Main:
    def __init__(self):
        self.a, self.b = map(int, input().split())

    def solve(self):
        g = gcd(self.a, self.b)
        print('1' * g)


problem = Main()
problem.solve()

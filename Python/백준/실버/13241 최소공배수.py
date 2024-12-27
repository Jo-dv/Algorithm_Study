from math import lcm


class Main:
    def __init__(self):
        self.a, self.b = map(int, input().split())

    def solve(self):
        print(lcm(self.a, self.b))


problem = Main()
problem.solve()
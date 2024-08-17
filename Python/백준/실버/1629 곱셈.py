class Main:
    def __init__(self):
        self.a, self.b, self.c = map(int, input().split())

    def power(self, a, b):
        if b == 1:
            return a % self.c

        if b % 2 == 0:
            x = self.power(a, b // 2)
            return (x * x) % self.c
        else:
            x = self.power(a, (b - 1) // 2)
            return (a * x * x) % self.c

    def solve(self):
        print(self.power(self.a, self.b))


problem = Main()
problem.solve()
class Main:
    def __init__(self):
        self.n = int(input())
        self.k = int(input())
        self.sensor = list(map(int, input().split()))

    def solve(self):
        self.sensor.sort()
        distance = sorted(list(map(lambda i: self.sensor[i + 1] - self.sensor[i], range(self.n - 1))))
        print(sum(distance[:self.n - self.k]))


problem = Main()
problem.solve()
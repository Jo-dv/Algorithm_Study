import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.files = [input() for _ in range(self.n)]
        self.extensions = set(input() for _ in range(self.m))

    def solve(self):
        result = []
        for file in self.files:
            name, extension = file.split('.')
            result.append((name, 0 if extension in self.extensions else 1, extension, file))

        result.sort(key=lambda x: (x[0], x[1], x[2]))
        
        for i in result:
            print(i[-1])


problem = Main()
problem.solve()
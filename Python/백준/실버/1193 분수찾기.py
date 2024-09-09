class Main:
    def __init__(self):
        self.x = int(input())

    def solve(self):
        line = 1

        while self.x > line:
            self.x -= line
            line += 1

        a = self.x if not line % 2 else line - self.x + 1
        b = line - self.x + 1 if not line % 2 else self.x

        print(f'{a}/{b}')


problem = Main()
problem.solve()
        
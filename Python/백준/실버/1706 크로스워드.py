class Main:
    def __init__(self):
        self.r, self.c = map(int, input().split())
        self.board = [input() for _ in range(self.r)]
        self.check = []
        self.result = []

    def solve(self):
        for i in zip(*self.board):
            temp = ""
            for j in i:
                temp += j
            self.check.append(temp.split("#"))

        for i in self.board:
            temp = ""
            for j in i:
                temp += j
            self.check.append(temp.split("#"))

        for i in self.check:
            for j in i:
                if len(j) > 1:
                    self.result.append(j)

        self.result.sort()
        print(self.result[0])


problem = Main()
problem.solve()

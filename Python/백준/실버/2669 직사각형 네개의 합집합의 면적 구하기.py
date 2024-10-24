class Main:
    def __init__(self):
        self.cord = [tuple(map(int, input().split())) for _ in range(4)]
        self.board = [[0] * 101 for _ in range(101)]
        self.answer = 0

    def solve(self):
        for c in self.cord:
            for y in range(c[1], c[3]):
                for x in range(c[0], c[2]):
                    self.board[y][x] = 1

        for i in self.board:
            self.answer += i.count(1)

        print(self.answer)


problem = Main()
problem.solve()
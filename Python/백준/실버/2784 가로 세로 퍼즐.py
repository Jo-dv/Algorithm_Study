class Main:
    def __init__(self):
        self.words = [input() for _ in range(6)]
        self.answer = None

    def make_puzzle(self, used, puzzle):
        if self.answer is not None:
            return
        if len(puzzle) == 3:
            self.check_valid(puzzle)
            return
        for i in range(6):
            if used[i]:
                continue
            used[i] = True
            self.make_puzzle(used, puzzle + [self.words[i]])
            used[i] = False

    def check_valid(self, puzzle):
        temp = self.words[:]
        for row in puzzle:
            if row in temp:
                temp.remove(row)
        for col in zip(*puzzle):
            col = "".join(col)
            if col in temp:
                temp.remove(col)

        if not temp:
            self.answer = "\n".join(i for i in puzzle)
            return

    def solve(self):
        self.make_puzzle([False] * 6, [])
        print(0 if self.answer is None else self.answer)


problem = Main()
problem.solve()

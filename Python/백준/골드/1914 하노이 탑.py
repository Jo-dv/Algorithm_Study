class Main:
    def __init__(self):
        self.n = int(input())

    def recur(self, idx, start, mid, end):
        if idx == 1:
            print(start, end)
            return

        self.recur(idx - 1, start, end, mid)
        print(start, end)
        self.recur(idx - 1, mid, start, end)

    def solve(self):
        print(2 ** self.n - 1)
        if self.n <= 20:
            self.recur(self.n, 1, 2, 3)


problem = Main()
problem.solve()

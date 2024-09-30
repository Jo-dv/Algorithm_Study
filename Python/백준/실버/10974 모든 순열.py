class Main:
    def __init__(self):
        self.n = int(input())
        self.visited = [False] * (self.n + 1)
        self.temp = []

    def search(self, idx):
        if idx == self.n:
            print(*self.temp)
            return
        for i in range(1, self.n + 1):
            if self.visited[i]:
                continue
            self.visited[i] = True
            self.temp.append(i)
            self.search(idx + 1)
            self.temp.pop()
            self.visited[i] = False

        return

    def solve(self):
        self.search(0)
        return


problem = Main()
problem.solve()

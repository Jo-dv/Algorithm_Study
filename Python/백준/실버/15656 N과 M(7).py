class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.arr = list(map(int, input().split()))
        self.answer = []

    def search(self, cnt):
        if cnt == self.m:
            print(*self.answer)
            return

        for i in range(self.n):
            self.answer.append(self.arr[i])
            self.search(cnt + 1)
            self.answer.pop()

        return

    def solve(self):
        self.arr.sort()
        self.search(0)


problem = Main()
problem.solve()

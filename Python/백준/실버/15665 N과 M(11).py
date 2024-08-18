class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.arr = set(map(int, input().split()))
        self.answer = []

    def search(self, cnt, max_size):
        if cnt == self.m:
            print(*self.answer)
            return

        for i in range(max_size):
            self.answer.append(self.arr[i])
            self.search(cnt + 1, max_size)
            self.answer.pop()

        return

    def solve(self):
        self.arr = list(self.arr)
        self.arr.sort()
        self.search(0, len(self.arr))
        return


problem = Main()
problem.solve()

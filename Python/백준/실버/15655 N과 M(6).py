class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.arr = list(map(int, input().split()))
        self.answer = []

    def back(self, idx, cnt):
        if idx == self.n:
            if cnt == self.m:
                print(*self.answer)
                return
            return

        self.answer.append(self.arr[idx])
        self.back(idx + 1, cnt + 1)
        self.answer.pop()
        self.back(idx + 1, cnt)

    def solve(self):
        self.arr.sort()
        self.back(0, 0)


problem = Main()
problem.solve()

class Main:
    def __init__(self):
        self.a, self.b = input().split()
        self.answer = float('inf')

    def solve(self):
        for i in range(len(self.b) - len(self.a) + 1):
            cnt = 0
            for j in range(len(self.a)):
                if self.a[j] != self.b[i + j]:
                    cnt += 1
            self.answer = min(self.answer, cnt)

        print(self.answer)


problem = Main()
problem.solve()
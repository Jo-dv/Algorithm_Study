class Main:
    def __init__(self):
        self.n, self.x = map(int, input().split())
        self.visitors = list(map(int, input().split()))
        self.answer = [0, 0]

    def solve(self):
        total = sum(self.visitors[:self.x])
        if total > self.answer[0]:
            self.answer[0] = total
            self.answer[1] = 1

        for i in range(self.x, self.n):
            total -= self.visitors[i - self.x]
            total += self.visitors[i]
            if total > self.answer[0]:
                self.answer[0] = total
                self.answer[1] = 1
            elif total == self.answer[0]:
                self.answer[1] += 1

        print("SAD" if self.answer[0] == 0 else str(self.answer[0]) + "\n" + str(self.answer[1]))


problem = Main()
problem.solve()
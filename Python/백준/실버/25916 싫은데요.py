class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.hole = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        low = 0
        current_weight = 0

        for high in range(self.n):
            current_weight += self.hole[high]
            while current_weight > self.m:
                current_weight -= self.hole[low]
                low += 1

            self.answer = max(self.answer, current_weight)

        print(self.answer)


problem = Main()
problem.solve()
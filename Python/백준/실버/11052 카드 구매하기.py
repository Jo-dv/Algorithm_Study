class Main:
    def __init__(self):
        self.n = int(input())
        self.packs = [0] + list(map(int, input().split()))

    def solve(self):
        costs = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            for j in range(1, i + 1):
                costs[i] = max(costs[i], self.packs[j] + costs[i - j])

        print(costs[self.n])


problem = Main()
problem.solve()
from itertools import permutations as pm


class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.weights = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        for weight in pm(self.weights, self.n):
            current_weight = 500
            for i in weight:
                current_weight += i
                current_weight -= self.k
                if current_weight < 500:
                    break
            else:
                self.answer += 1
        print(self.answer)


problem = Main()
problem.solve()
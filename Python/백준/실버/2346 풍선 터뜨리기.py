from collections import deque


class Main:
    def __init__(self):
        self.n = int(input())
        self.balloons = list(map(int, input().split()))
        self.answer = []

    def solve(self):
        self.balloons = deque((num, balloon) for num, balloon in enumerate(self.balloons, 1))
        while self.balloons:
            idx, balloon = self.balloons[0]
            self.balloons.popleft()
            self.answer.append(idx)
            self.balloons.rotate(-balloon + (1 if balloon > 0 else 0))

        print(*self.answer)


problem = Main()
problem.solve()
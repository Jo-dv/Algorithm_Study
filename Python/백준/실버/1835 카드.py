from collections import deque


class Main:
    def __init__(self):
        self.n = int(input())

    def solve(self):
        deck = deque([self.n])

        for i in range(self.n - 1, 0, -1):
            deck.appendleft(i)
            for _ in range(i):
                deck.appendleft(deck.pop())

        print(*deck)


problem = Main()
problem.solve()
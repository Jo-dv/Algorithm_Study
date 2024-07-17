import sys
import heapq
from collections import deque

input = lambda: sys.stdin.readline()


class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.jewels = [tuple(map(int, input().split())) for _ in range(self.n)]
        self.bags = [int(input()) for _ in range(self.k)]
        self.answer = 0

    def solve(self):
        self.jewels.sort()
        self.bags.sort()

        self.jewels = deque(self.jewels)
        heap = []

        for bag in self.bags:
            while self.jewels and self.jewels[0][0] <= bag:
                heapq.heappush(heap, -self.jewels[0][1])
                self.jewels.popleft()

            if heap:
                self.answer += abs(heapq.heappop(heap))

        print(self.answer)


problem = Main()
problem.solve()
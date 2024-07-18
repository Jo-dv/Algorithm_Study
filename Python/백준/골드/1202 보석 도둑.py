import sys
import heapq

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

        heap = []
        i = 0

        for bag in self.bags:
            while i < self.n and self.jewels[i][0] <= bag:
                heapq.heappush(heap, -self.jewels[i][1])
                i += 1

            if heap:
                self.answer += abs(heapq.heappop(heap))

        print(self.answer)


problem = Main()
problem.solve()
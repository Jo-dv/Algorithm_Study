from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m, self.k, self.x = map(int, input().split())
        self.info = [tuple(map(int, input().split())) for _ in range(self.m)]
        self.answer = []

    def solve(self):
        graph = {i + 1: [] for i in range(self.n)}
        for a, b in self.info:
            graph[a].append(b)

        visited = [False] * (self.n + 1)
        dq = deque([(self.x, 0)])
        visited[self.x] = True

        while dq:
            current, distance = dq.popleft()
            if distance == self.k:
                self.answer.append(current)
            for nxt in graph[current]:
                if not visited[nxt]:
                    visited[nxt] = True
                    dq.append((nxt, distance + 1))

        if not self.answer:
            print(-1)
        else:
            self.answer.sort()
            for i in self.answer:
                print(i)


problem = Main()
problem.solve()
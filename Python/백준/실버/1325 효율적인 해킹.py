import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.graph = defaultdict(list)
        self.depth = [0] * (self.n + 1)

    def bfs(self, start):
        visited = [False] * (self.n + 1)
        visited[start] = True
        dq = deque([start])
        count = 0

        while dq:
            current = dq.popleft()
            for nxt in self.graph[current]:
                if not visited[nxt]:
                    visited[nxt] = True
                    dq.append(nxt)
                    count += 1

        return count

    def solve(self):
        for _ in range(self.m):
            a, b = map(int, input().split())
            self.graph[b].append(a)

        max_depth = 0
        answer = []

        for i in range(1, self.n + 1):
            depth = self.bfs(i)
            if depth > max_depth:
                max_depth = depth
                answer = [i]
            elif depth == max_depth:
                answer.append(i)

        print(*answer)


problem = Main()
problem.solve()
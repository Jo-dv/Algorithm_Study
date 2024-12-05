from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.info = [tuple(map(int, input().split())) for _ in range(self.m)]
        self.answer = 0

    def search(self, graph: dict[int, list], degree: list[int], visited: list[bool], current: int):
        for nxt in graph[current]:
            if not visited[nxt]:
                visited[nxt] = True
                degree[nxt] += 1
                self.search(graph, degree, visited, nxt)
        return

    def solve(self):
        in_graph = defaultdict(list)
        out_graph = defaultdict(list)
        in_degree = [0] * (self.n + 1)
        out_degree = [0] * (self.n + 1)

        for a, b in self.info:
            in_graph[b].append(a)
            out_graph[a].append(b)

        for i in range(1, self.n + 1):
            visited = [False] * (self.n + 1)
            visited[i] = True
            self.search(in_graph, in_degree, visited, i)
            self.search(out_graph, out_degree, visited, i)

        for i in range(1, self.n + 1):
            if in_degree[i] + out_degree[i] == self.n - 1:
                self.answer += 1

        print(self.answer)


problem = Main()
problem.solve()

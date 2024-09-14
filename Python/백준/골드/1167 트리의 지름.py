import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, n, w):
        self.n = n
        self.w = w


class Main:
    def __init__(self):
        self.v = int(input())
        self.nodes = [list(map(int, input().split())) for _ in range(self.v)]

    def dfs(self, start: int, weight: int, graph: list[list[Node]], visited: list[int]):
        for node in graph[start]:
            if visited[node.n] == -1:
                visited[node.n] = weight + node.w
                self.dfs(node.n, weight + node.w, graph, visited)

    def solve(self):
        graph: list[list[Node]] = [[] for _ in range(self.v + 1)]

        for node in self.nodes:
            parent = node[0]
            for i in range(1, len(node), 2):
                nxt = node[i:i + 2]
                if nxt[0] != -1:
                    child, weight = nxt
                    graph[parent].append(Node(child, weight))

        visited = [-1] * (self.v + 1)
        visited[self.v] = 0
        self.dfs(self.v, visited[self.v], graph, visited)

        distant = visited.index(max(visited))
        visited = [-1] * (self.v + 1)
        visited[distant] = 0
        self.dfs(distant, visited[distant], graph, visited)

        print(max(visited))


problem = Main()
problem.solve()
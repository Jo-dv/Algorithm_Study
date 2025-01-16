class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.nodes = [tuple(map(int, input().split())) for _ in range(self.n - 1)]
        self.problem = [tuple(map(int, input().split())) for _ in range(self.m)]
        self.graph = {i: [] for i in range(1, self.n + 1)}

    def search(self, current, goal, total_distance, visited):
        visited[current] = True

        if current == goal:
            print(total_distance)
            return

        for node in self.graph[current]:
            nxt, distance = node
            if not visited[nxt]:
                self.search(nxt, goal, total_distance + distance, visited)

    def solve(self):
        for node in self.nodes:
            u, v, d = node
            self.graph[u].append((v, d))
            self.graph[v].append((u, d))

        for start, goal in self.problem:
            self.search(start, goal, 0, [False] * (self.n + 1))


problem = Main()
problem.solve()

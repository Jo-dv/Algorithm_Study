import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.nums = [int(input()) for _ in range(self.n)]
        self.visited = set()
        self.answer = []

    def search(self, graph, i):
        self.visited.add(i)

        for node in graph[i]:
            if node not in self.visited:
                self.search(graph, node)
            else:
                self.answer.append(node)
        return

    def solve(self):
        graph = {i: [] for i in range(1, self.n + 1)}
        for i, num in enumerate(self.nums, 1):
            graph[num].append(i)

        for i in range(1, self.n + 1):
            self.visited = set()
            self.search(graph, i)

        print(len(self.answer))
        for i in self.answer:
            print(i)


problem = Main()
problem.solve()

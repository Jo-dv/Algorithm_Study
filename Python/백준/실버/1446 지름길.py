import heapq


class Main:
    def __init__(self):
        self.n, self.d = map(int, input().split())
        self.nodes = [tuple(map(int, input().split())) for _ in range(self.n)]
        self.graph = [[] for _ in range(self.d + 1)]

    def init_graph(self):
        for i in range(self.d):
            self.graph[i].append((1, i + 1))  # distance, destination

        for node in self.nodes:
            start, end, length = node
            if end <= self.d:
                self.graph[start].append((length, end))

    def dijkstra(self):
        hq = []
        distance = [float('inf') for _ in range(self.d + 1)]
        heapq.heappush(hq, (0, 0))
        distance[0] = 0

        while hq:
            current_distance, current = heapq.heappop(hq)

            for i in self.graph[current]:
                nxt_distance, nxt = i
                if current_distance + nxt_distance < distance[nxt]:
                    distance[nxt] = current_distance + nxt_distance
                    heapq.heappush(hq, (current_distance + nxt_distance, nxt))

        print(distance[self.d])

    def solve(self):
        self.init_graph()
        self.dijkstra()


problem = Main()
problem.solve()
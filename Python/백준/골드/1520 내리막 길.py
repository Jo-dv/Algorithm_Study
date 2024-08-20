import sys
sys.setrecursionlimit(10**5)


class Main:
    def __init__(self):
        self.m, self.n = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.m)]
        self.visited = [[-1] * self.n for _ in range(self.m)]
        # -1은 방문하지 않은 것을 의미, 0으로 초기화하지 않는 이유는 0도 경우의 수이기 때문(해당 지점에서 갈 수 없는 경우)
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def dfs(self, y, x):
        if y == self.m - 1 and x == self.n - 1:
            return 1

        if self.visited[y][x] != -1:  # 방문한 곳이라면
            return self.visited[y][x]

        self.visited[y][x] = 0  # 일단 도착할 수 있는지 알 수 없으므로 0으로 변경
        for d in self.directions:
            my = y + d[0]
            mx = x + d[1]
            if 0 <= my < self.m and 0 <= mx < self.n and self.grid[my][mx] < self.grid[y][x]:
                self.visited[y][x] += self.dfs(my, mx)  # 경우의 수 합산

        return self.visited[y][x]  # 각 지점에서 시작했을 때, 목적지에 도착할 수 있는 경우의 수를 저장

    def solve(self):
        print(self.dfs(0, 0))


problem = Main()
problem.solve()
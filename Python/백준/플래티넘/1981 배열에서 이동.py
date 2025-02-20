from collections import deque


class Main:
    def __init__(self):
        self.n = int(input())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.answer = 0

    def search(self, min_num, max_num):
        if not (min_num <= self.grid[0][0] <= max_num):
            return False  # 시작점이 범위를 벗어나면 불가능

        queue = deque([(0, 0)])
        visited = [[False] * self.n for _ in range(self.n)]
        visited[0][0] = True

        while queue:
            y, x = queue.popleft()
            if y == self.n - 1 and x == self.n - 1:
                return True  # 목적지 도착 가능

            for dy, dx in self.directions:
                my, mx = y + dy, x + dx

                if 0 <= my < self.n and 0 <= mx < self.n and not visited[my][mx]:
                    if min_num <= self.grid[my][mx] <= max_num:
                        visited[my][mx] = True
                        queue.append((my, mx))

        return False  # 끝까지 도달하지 못하면 False
    
    def solve(self):
        min_num, max_num = min(map(min, self.grid)), max(map(max, self.grid))
        left, right = 0, max_num - min_num
        self.answer = right  # 가능한 최소 차이를 저장

        while left <= right:
            mid = (left + right) // 2
            found = False  # min_num ~ min_num + mid 범위 내에서 BFS가 가능한지 확인

            for start in range(min_num, max_num - mid + 1):
                if self.search(start, start + mid):
                    found = True
                    break

            if found:
                self.answer = mid
                right = mid - 1  # 더 작은 차이로 줄임
            else:
                left = mid + 1  # 차이를 늘림

        print(self.answer)


problem = Main()
problem.solve()
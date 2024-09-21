from collections import deque


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.answer = 0

    def count_cheese(self):
        return sum(sum(i) for i in self.grid)

    def split_space(self):
        dq = deque([(0, 0)])
        visited = [[False] * self.m for _ in range(self.n)]

        while dq:
            y, x = dq.popleft()

            for dy, dx in self.directions:
                my = y + dy
                mx = x + dx
                if 0 <= my < self.n and 0 <= mx < self.m and not visited[my][mx] and self.grid[my][mx] != 1:
                    visited[my][mx] = True
                    self.grid[my][mx] = 10
                    dq.append((my, mx))

    def melt(self):
        dq = deque([(0, 0)])
        visited = [[False] * self.m for _ in range(self.n)]
        cheese = []  # 발견한 치즈를 저장
        melted_cheese = []  # 녹일 치즈를 저장
        
        while dq:
            y, x = dq.popleft()

            for dy, dx in self.directions:
                my = y + dy
                mx = x + dx
                if 0 <= my < self.n and 0 <= mx < self.m and not visited[my][mx]:
                    visited[my][mx] = True
                    if self.grid[my][mx] == 10:
                        dq.append((my, mx))
                    else:
                        cheese.append((my, mx))

        while cheese:
            y, x = cheese.pop()
            space = 0

            for dy, dx in self.directions:
                my = y + dy
                mx = x + dx

                if 0 <= my < self.n and 0 <= mx < self.m and self.grid[my][mx] == 10:
                    space += 1
                    if space >= 2:
                        melted_cheese.append((y, x))
                        break

        for y, x in melted_cheese:  # 치즈를 발견하는 과정에서 바로 녹이면 빈 공간이 되면서 다른 치즈에 영향을 줌
            self.grid[y][x] = 10
            
        return len(melted_cheese)  # 녹인 치즈의 수 반환

    def solve(self):
        rest_cheese = self.count_cheese()

        while rest_cheese:
            self.split_space()  # 내부 외부 공간 구분
            rest_cheese -= self.melt()

            self.answer += 1

        print(self.answer)


problem = Main()
problem.solve()
import sys
input = lambda: sys.stdin.readline()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.move_info = [tuple(map(int, input().split())) for _ in range(self.m)]
        self.move_directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        self.water_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def create_cloud(self):
        return [(self.n - 1, 0), (self.n - 1, 1), (self.n - 2, 0), (self.n - 2, 1)]

    def move_cloud(self, clouds: list, d, s):
        result = set()  # 이동 및 비내리기가 끝난 구름들을 저장할 자료 구조

        dy, dx = self.move_directions[d - 1]
        my = dy * s
        mx = dx * s
        while clouds:  # 현재 구름들 기준
            y, x = clouds.pop()  # 자연스럽게 구름 제거
            y = (y + my) % self.n  # 경계를 넘을 때 돌아오기 위함
            x = (x + mx) % self.n
            self.grid[y][x] += 1
            result.add((y, x))

        return result

    def copy_water(self, result):
        for y, x in result:  # 물복사 버그
            cnt = 0
            for dy, dx in self.water_directions:
                my = y + dy
                mx = x + dx
                if 0 <= my < self.n and 0 <= mx < self.n and self.grid[my][mx] != 0:
                    cnt += 1
            self.grid[y][x] += cnt

    def make_clouds(self, clouds, result):
        for y in range(self.n):
            for x in range(self.n):
                if (y, x) not in result and self.grid[y][x] >= 2:
                    self.grid[y][x] -= 2
                    clouds.append((y, x))

    def count_water(self):
        return sum(map(sum, self.grid))

    def solve(self):
        clouds = self.create_cloud()  # 구름 생성

        for d, s in self.move_info:
            result = self.move_cloud(clouds, d, s)  # 구름 이동
            self.copy_water(result)  # 비복사
            self.make_clouds(clouds, result)  # 새로운 비구름 생성

        print(self.count_water())


problem = Main()
problem.solve()
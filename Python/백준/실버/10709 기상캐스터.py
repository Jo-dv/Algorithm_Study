class Main:
    def __init__(self):
        self.h, self.w = map(int, input().split())
        self.grid = [list(input()) for _ in range(self.h)]
        self.answer = [[-1] * self.w for _ in range(self.h)]

    def init_clouds(self):  # 구름의 초기 위치 초기화
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x] == 'c':
                    self.answer[y][x] = 0

    def search_clouds(self):  # 이동을 위해 구름들의 위치 탐색
        return [(y, x) for x in range(self.w) for y in range(self.h) if self.grid[y][x] == 'c']

    def move_clouds(self, clouds: list):  # 탐색된 구름들을 바탕으로 이동
        for y, x in clouds:
            mx = x + 1  # 현재 위치에서 바로 다음
            while mx < self.w:  # 유효하다면
                if self.answer[y][mx] == -1:  # 다음으로 이동하는 위치가 처음으로 구름이 이동하는 곳이라면
                    self.answer[y][mx] = (self.answer[y][x] + 1)  # 이전 시간 바탕으로 시간 갱신
                    x = mx  # 이동이 끝났기 때문에 다음 위치를 현재 위치로 갱신
                    mx += 1  # 현재 위치의 갱신이 끝났으므로 다음 위치 갱신
                else:  # 이미 구름이 지나간 자리라면
                    break  # 해당 구름 이동 종료

    def solve(self):
        self.init_clouds()
        clouds = self.search_clouds()
        self.move_clouds(clouds)

        for i in self.answer:
            print(*i)


problem = Main()
problem.solve()

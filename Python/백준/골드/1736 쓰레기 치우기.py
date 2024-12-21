class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.trash = 0
        self.answer = 0

    def find_trash(self):
        for y in range(self.n):
            for x in range(self.m):
                if self.grid[y][x]:
                    self.trash += 1

    def search_trash(self, start_y, start_x):
        for y in range(start_y, self.n):  # 제시된 방향에 맞춰 탐색
            for x in range(start_x, self.m):
                if self.grid[y][x]:  # 쓰레기 발견
                    self.grid[y][x] = 0
                    self.trash -= 1
                    if self.trash == 0:
                        return
                    self.search_trash(y, x)  # 현재 위치를 기점으로 재탐색 -> 탐색 범위 제한
                    return

    def solve(self):
        self.find_trash()
        while self.trash:  # 쓰레기가 있다면
            self.answer += 1  # 로봇 출발
            self.search_trash(0, 0)  # 로봇들의 출발 위치

        print(self.answer)


problem = Main()
problem.solve()
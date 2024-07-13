class shark:
    def __init__(self, r, c, s, d, z):
        self.r = r
        self.c = c
        self.speed = s
        self.direction = d
        self.size = z


class Main:
    def __init__(self):
        self.r, self.c, self.m = map(int, input().split())
        self.info = [list(map(int, input().split())) for _ in range(self.m)]
        self.grid = [[None] * self.c for _ in range(self.r)]
        self.sharks = []
        self.answer = 0

    def init_grid(self):
        for r, c, s, d, z in self.info:
            shark_info = shark(r-1, c-1, s, d, z)  # (r, c), s=속도, d=방향(1: 상, 2: 하, 3: 우, 4: 좌), z=크기
            self.grid[r-1][c-1] = shark_info
            self.sharks.append(shark_info)

    def fishing(self, c):
        get_shark: shark
        for r in range(self.r):  # 땅과 가까운 순서대로
            if self.grid[r][c] is not None:  # 상어가 있다면
                get_shark = self.grid[r][c]
                self.sharks.remove(get_shark)
                self.answer += get_shark.size
                break  # 한 번 잡으면 끝
        return

    def move_shark(self):
        current_shark: shark
        for current_shark in self.sharks:
            if current_shark.direction in [1, 2]:  # 상, 하
                for _ in range(current_shark.speed % ((self.r - 1) * 2)):
                    if current_shark.r == 0:
                        current_shark.direction = 2
                    elif current_shark.r == self.r-1:
                        current_shark.direction = 1
                    current_shark.r += -1 if current_shark.direction == 1 else 1
            else:  # 우, 좌
                for _ in range(current_shark.speed % ((self.c - 1) * 2)):
                    if current_shark.c == 0:
                        current_shark.direction = 3
                    elif current_shark.c == self.c - 1:
                        current_shark.direction = 4
                    current_shark.c += 1 if current_shark.direction == 3 else -1

    def clear_grid(self):
        self.grid = [[None] * self.c for _ in range(self.r)]

    def eat_shark(self):
        self.clear_grid()  # 새롭게 상어를 배치할 것이므로 격자 초기화

        for current_shark in self.sharks[::-1]:  # 순서대로 상어를 이동시켰으므로 역순으로 해야 순서대로 탐색 가능
            if self.grid[current_shark.r][current_shark.c] is None:  # 상어가 없다면
                self.grid[current_shark.r][current_shark.c] = current_shark
            else:  # 상어를 위치시키려는 곳에 상어가 있다면
                if self.grid[current_shark.r][current_shark.c].size > current_shark.size:  # 현재 상어 잡아먹힘
                    self.sharks.remove(current_shark)
                else:  # 기존 상어 잡아 먹음 -> 어차피 크기가 큰 상어가 나중에 다 잡아먹기 때문에 크기가 같아도 지금 잡아먹어도 됨
                    self.sharks.remove(self.grid[current_shark.r][current_shark.c])
                    self.grid[current_shark.r][current_shark.c] = current_shark

    def solve(self):
        self.init_grid()

        for i in range(self.c):  # 낚시왕 이동
            self.fishing(i)  # 낚시 시작
            self.move_shark()  # 상어 이동
            self.eat_shark()  # 상어 경쟁

        print(self.answer)


problem = Main()
problem.solve()
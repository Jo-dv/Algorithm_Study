from collections import deque


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.grid = [list(map(int, input())) for _ in range(self.n)]
        self.area = [[0] * self.m for _ in range(self.n)]

    def check_range(self, y, x):
        return 0 <= y < self.n and 0 <= x < self.m and (y, x)

    def search_area(self):
        dq = deque([])
        info = {}
        num = 1

        for y in range(self.n):
            for x in range(self.m):
                if self.grid[y][x] == 0 and self.area[y][x] == 0:  # 텅 빈 영역 탐색
                    dq.append((y, x))
                    self.area[y][x] = num
                    cnt = 1

                    while dq:
                        current_y, current_x = dq.popleft()
                        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            my, mx = current_y + dy, current_x + dx
                            if self.check_range(my, mx) and self.area[my][mx] == 0 and self.grid[my][mx] == 0:
                                dq.append((my, mx))
                                self.area[my][mx] = num
                                cnt += 1  # 영역의 수 갱신

                    info[num] = cnt  # 해당 영역 마킹
                    num += 1

        return info

    def get_result(self, info):
        for y in range(self.n):
            for x in range(self.m):
                if self.grid[y][x] == 1:
                    check_used = set()
                    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        my, mx = y + dy, x + dx
                        if self.check_range(my, mx):
                            num = self.area[my][mx]  # 해당 영역이 어디에 해당하는지
                            if num and num not in check_used:  # 텅 빈 영역이 아니고 아직 합산하지 않았다면
                                self.grid[y][x] += info[num]
                                check_used.add(num)
                    self.grid[y][x] %= 10

    def solve(self):
        info = self.search_area()
        self.get_result(info)

        print("\n".join("".join(map(str, i)) for i in self.grid))


problem = Main()
problem.solve()
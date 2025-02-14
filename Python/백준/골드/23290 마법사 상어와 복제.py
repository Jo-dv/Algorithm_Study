from itertools import product as pd
from collections import defaultdict


class Main:
    def __init__(self):
        self.m, self.s = map(int, input().split())
        self.fish_info = defaultdict(int)  # (y, x, d) -> count 형태로 저장
        for _ in range(self.m):
            fy, fx, fd = map(lambda x: int(x) - 1, input().split())
            self.fish_info[(fy, fx, fd)] += 1  # 같은 위치, 같은 방향 물고기 합치기
        self.sy, self.sx = map(lambda x: int(x) - 1, input().split())
        self.fish_directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        self.shark_directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.priority = list(pd([0, 1, 2, 3], repeat=3))
        self.grid = [[0] * 4 for _ in range(4)]
        self.copy_fish_info = defaultdict(int)
        self.smells = [[0] * 4 for _ in range(4)]
        self.answer = 0

    def init_grid(self):
        for (fy, fx, _), count in self.fish_info.items():
            self.grid[fy][fx] += count

    def do_copy(self):
        self.copy_fish_info = self.fish_info.copy()

    def move_fish(self):
        new_fish_info = defaultdict(int)

        for (fy, fx, fd), count in self.fish_info.items():
            for i in range(8):
                dy, dx = self.fish_directions[(fd - i) % 8]
                my, mx = fy + dy, fx + dx
                if 0 <= my < 4 and 0 <= mx < 4 and (my, mx) != (self.sy, self.sx) and self.smells[my][mx] == 0:
                    new_fish_info[(my, mx, (fd - i) % 8)] += count  # 이동 후 중복된 방향은 합치기
                    break
            else:
                new_fish_info[(fy, fx, fd)] += count  # 이동 불가 시 원래 위치 유지

        self.fish_info = new_fish_info

    def move_shark(self):
        max_cnt = -1
        best_route = []
        best_pos = (self.sy, self.sx)

        for direction in self.priority:
            my, mx = self.sy, self.sx
            visited = set()
            cnt = 0

            for d in direction:
                dy, dx = self.shark_directions[d]
                my += dy
                mx += dx
                if 0 <= my < 4 and 0 <= mx < 4:
                    visited.add((my, mx))
                else:
                    break
            else:
                for (fy, fx, fd), count in self.fish_info.items():
                    if (fy, fx) in visited:
                        cnt += count

                if cnt > max_cnt:
                    max_cnt = cnt
                    best_route = visited
                    best_pos = (my, mx)

        if best_route:
            new_fish_info = defaultdict(int)
            for key, count in self.fish_info.items():
                fy, fx, fd = key
                if (fy, fx) in best_route:
                    self.smells[fy][fx] = 3  # 물고기 냄새 남기기
                else:
                    new_fish_info[key] = count

            self.fish_info = new_fish_info
            self.sy, self.sx = best_pos

    def clear_smell(self):
        for y in range(4):
            for x in range(4):
                if self.smells[y][x] > 0:
                    self.smells[y][x] -= 1

    def done_copy(self):
        for key, count in self.copy_fish_info.items():
            self.fish_info[key] += count  # 동일 위치, 동일 방향의 물고기를 합침

    def get_fish(self):
        self.answer = sum(self.fish_info.values())

    def solve(self):
        self.init_grid()

        for _ in range(self.s):
            self.do_copy()
            self.move_fish()
            self.move_shark()
            self.clear_smell()
            self.done_copy()

        self.get_fish()
        print(self.answer)


problem = Main()
problem.solve()

# class Main:
#     def __init__(self):
#         self.m, self.s = map(int, input().split())
#         self.fish_info = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(self.m)]
#         self.sy, self.sx = map(lambda x: int(x) - 1, input().split())
#         self.fish_directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
#         self.shark_directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
#         self.priority = list(pd([0, 1, 2, 3], repeat=3))
#         self.grid = [[0] * 4 for _ in range(4)]
#         self.copy_fish_info = list()
#         self.smells = [[0] * 4 for _ in range(4)]
#         self.answer = 0
#
#     def init_grid(self):
#         for fish in self.fish_info:
#             fy, fx, fd = fish
#             self.grid[fy][fx] += 1
#
#     def do_copy(self):
#         self.copy_fish_info = [fish[:] for fish in self.fish_info]
#
#     def move_fish(self):
#         for fish in range(len(self.fish_info)):
#             fy, fx, fd = self.fish_info[fish]
#             for i in range(8):
#                 dy, dx = self.fish_directions[(fd - i) % 8]
#                 my, mx = fy + dy, fx + dx
#                 if 0 <= my < 4 and 0 <= mx < 4 and (my, mx) != (self.sy, self.sx) and self.smells[my][mx] == 0:
#                     self.grid[fy][fx] -= 1
#                     self.grid[my][mx] += 1
#                     self.fish_info[fish] = (my, mx, (fd - i) % 8)
#                     break
#
#     def move_shark(self):
#         max_cnt = -1
#         final_route = []
#
#         for direction in self.priority:
#             my, mx = self.sy, self.sx
#             route = []
#             cnt = 0
#             visited = set()
#
#             for d in direction:
#                 dy, dx = self.shark_directions[d]
#                 my += dy
#                 mx += dx
#                 if 0 <= my < 4 and 0 <= mx < 4:
#                     if (my, mx) not in visited:
#                         cnt += self.grid[my][mx]
#                     route.append((my, mx))
#                     visited.add((my, mx))
#                 else:
#                     break
#             else:
#                 if max_cnt < cnt:
#                     max_cnt = cnt
#                     final_route = route
#
#         if final_route:
#             for fish in range(len(self.fish_info) - 1, -1, -1):
#                 fy, fx, fd = self.fish_info[fish]
#                 if (fy, fx) in final_route:
#                     self.grid[fy][fx] -= 1
#                     self.smells[fy][fx] = 3
#                     self.fish_info.pop(fish)
#
#             self.sy, self.sx = final_route[-1]
#
#     def clear_smell(self):
#         for y in range(4):
#             for x in range(4):
#                 if self.smells[y][x] > 0:
#                     self.smells[y][x] -= 1
#
#     def done_copy(self):
#         for copy_fish in range(len(self.copy_fish_info) - 1, -1, -1):
#             fy, fx, fd = self.copy_fish_info[copy_fish]
#             self.grid[fy][fx] += 1
#             self.fish_info.append((fy, fx, fd))
#             self.copy_fish_info.pop()
#
#     def get_fish(self):
#         for i in self.grid:
#             for j in i:
#                 if j > 0:
#                     self.answer += j
#
#     def solve(self):
#         self.init_grid()
#
#         for t in range(1, self.s + 1):
#             self.do_copy()
#             self.move_fish()
#             self.move_shark()
#             self.clear_smell()
#             self.done_copy()
#
#         self.get_fish()
#         print(self.answer)

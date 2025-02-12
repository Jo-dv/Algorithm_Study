from collections import defaultdict


class Main:
    def __init__(self):
        self.n = int(input())
        self.student_info = [tuple(map(int, input().split())) for _ in range(self.n**2)]
        self.score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
        self.grid = [[0] * self.n for _ in range(self.n)]
        self.friends_list = defaultdict(set)
        self.answer = 0

    def init_structure(self):
        for i in self.student_info:
            student, like = i[0], set(i[1:])
            self.friends_list[student] = like

    def search(self):
        for i in self.student_info:
            student = i[0]
            max_friend_cnt = max_empty_cnt = -1
            for y in range(self.n):
                for x in range(self.n):
                    if self.grid[y][x] != 0:
                        continue
                    friend_cnt = empty_cnt = 0
                    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        my, mx = y + dy, x + dx
                        if 0 <= my < self.n and 0 <= mx < self.n:
                            if self.grid[my][mx] == 0:
                                empty_cnt += 1
                            if self.grid[my][mx] in self.friends_list[student]:
                                friend_cnt += 1

                    if max_friend_cnt < friend_cnt or (max_friend_cnt == friend_cnt and max_empty_cnt < empty_cnt):
                        max_friend_cnt = friend_cnt
                        max_empty_cnt = empty_cnt
                        ey, ex = y, x

            self.grid[ey][ex] = student

    def get_score(self):
        for y in range(self.n):
            for x in range(self.n):
                cnt = 0
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    my, mx = y + dy, x + dx
                    student = self.grid[y][x]
                    if 0 <= my < self.n and 0 <= mx < self.n and self.grid[my][mx] in self.friends_list[student]:
                        cnt += 1

                self.answer += self.score[cnt]

    def solve(self):
        self.init_structure()
        self.search()
        self.get_score()

        print(self.answer)


problem = Main()
problem.solve()
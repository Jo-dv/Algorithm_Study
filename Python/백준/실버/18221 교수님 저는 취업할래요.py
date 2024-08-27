class Main:
    def __init__(self):
        self.n = int(input())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]

    def search_pos(self):
        students = []
        prisoner = None
        professor = None

        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    students.append((i, j))  # (y, x)
                elif self.grid[i][j] == 2:
                    prisoner = (i, j)
                elif self.grid[i][j] == 5:
                    professor = (i, j)

        return students, prisoner, professor

    def solve(self):
        students, prisoner, professor = self.search_pos()  # 학생들, 성규, 교수님의 위치 탐색
        y1, x1 = prisoner
        y2, x2 = professor

        if (y1 - y2) ** 2 + (x1 - x2) ** 2 < 25:  # 성규와 교수님의 거리
            print(0)
            return

        cnt = 0
        for y, x in students:
            if min(y1, y2) <= y <= max(y1, y2) and min(x1, x2) <= x <= max(x1, x2):
                cnt += 1
                if cnt >= 3:  # 학생이 충분한 경우
                    print(1)
                    return

        print(0)


problem = Main()
problem.solve()

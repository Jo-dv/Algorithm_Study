from collections import deque


class Main:
    def __init__(self):
        self.stage = [list(input()) for _ in range(12)]
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우
        self.visited = None
        self.answer = 0

    def is_valid(self, y, x, my, mx):
        # 유효 범위면서 연속적일 때
        return 0 <= my < 12 and 0 <= mx < 6 and not self.visited[my][mx] and self.stage[y][x] == self.stage[my][mx]

    def search(self, start_y, start_x):  # 4개 이상의 뿌요들이 연속되어 있는지 탐색
        dq = deque([(start_y, start_x)])  # bfs 구현을 위한 deque 초기화
        self.visited[start_y][start_x] = True
        result = [(start_y, start_x)]  # 제거될 뿌요를 담을 리스트

        while dq:
            y, x = dq.popleft()

            for d in self.directions:
                my, mx = y + d[0], x + d[1]

                if self.is_valid(y, x, my, mx):
                    dq.append((my, mx))
                    self.visited[my][mx] = True
                    result.append((my, mx))

        return result

    def remove(self, result):  # 연속된 뿌요들 제거
        for y, x in result:
            self.stage[y][x] = "."
        return

    def down(self):  # 터진 뿌요들의 빈공간을 위의 뿌요들을 끌어내려서 채움
        for x in range(6):
            for i in range(10, -1, -1):  # 항상 y보다 위를 가리킴
                for y in range(11, i, -1):
                    if self.stage[i][x] != "." and self.stage[y][x] == ".":  # 뿌요면서 아래에 공간이 있다면
                        self.stage[y][x] = self.stage[i][x]  # 뿌요를 끌어내림
                        self.stage[i][x] = "."  # 뿌요가 끌어내려진 자리를 빈공간으로 변경

        self.answer += 1
        return

    def solve(self):
        while True:
            clear = False  # 뿌요들이 터질 때마다 종료 조건 초기화
            self.visited = [[False] * 6 for _ in range(12)]  # 뿌요들이 터질 때마다 방문 유무 초기화

            for y in range(12):  # 현재 탐색에서 터질 수 있는 뿌요는 모두 한 번에 터져야 하므로 모든 경우 탐색
                for x in range(6):
                    if self.stage[y][x] != "." and not self.visited[y][x]:
                        result = self.search(y, x)
                        if len(result) >= 4:  # 연속적인 뿌요가 있다면
                            clear = True  #
                            self.remove(result)  # 뿌요 제거

            if not clear:  # 더 이상 터질 뿌요가 없다면
                break

            self.down()  # 제거된 자리에 뿌요를 끌어내림

        print(self.answer)


problem = Main()
problem.solve()
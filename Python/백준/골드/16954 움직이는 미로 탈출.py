from collections import deque


class Main:
    def __init__(self):
        self.grid = [list(input()) for _ in range(8)]
        self.walls = set((i, j) for i in range(8) for j in range(8) if self.grid[i][j] == '#')

    def move_wall(self):
        next_walls = set()
        for x in range(8):
            for y in range(7, -1, -1):
                if self.grid[y][x] == '#':
                    self.grid[y][x] = '.'
                    if y < 7:
                        self.grid[y + 1][x] = '#'
                        next_walls.add((y + 1, x))

        self.walls = next_walls

    def move_wook(self):
        dq = deque([(7, 0, 0)])
        visited = {(7, 0, 0)}  # 가만히 있는 선택지도 있으므로 시점을 추가

        while dq:
            for _ in range(len(dq)):  # 현재 시점 처리, 즉 임의의 t일 때 큐에 들어온 값을 모두 처리해야 함
                y, x, t = dq.popleft()
                if y == 0 and x == 7:
                    print(1)
                    return

                if (y, x) in self.walls:  # 움직인 벽에 접촉되는 지점들이 있다면 무시
                    continue
    
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]:
                    my, mx = y + dy, x + dx
                    if 0 <= my < 8 and 0 <= mx < 8 and self.grid[my][mx] == '.' and (my, mx, t + 1) not in visited:
                        dq.append((my, mx, t + 1))
                        visited.add((my, mx, t + 1))
    
            if self.walls:
                self.move_wall()

        print(0)

    def solve(self):
        self.move_wook()


problem = Main()
problem.solve()

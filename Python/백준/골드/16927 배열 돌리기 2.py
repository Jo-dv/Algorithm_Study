import sys
input = lambda: sys.stdin.readline()


class Main:
    def __init__(self):
        self.n, self.m, self.r = map(int, input().split())
        self.arr = [list(map(int, input().split())) for _ in range(self.n)]

    def rotate(self, layer):  # 겉에서 부터 안으로
        perimeter = 2 * ((self.n - 2 * layer) + (self.m - 2 * layer) - 2)  # 현재 층의 둘레 계산
        actual_rotations = self.r % perimeter  # 실제 필요한 회전 횟수 계산
        y = self.n - layer - 1
        x = self.m - layer - 1

        for _ in range(actual_rotations):
            top_left = self.arr[layer][layer]  # 초기 값을 저장

            for i in range(layer, x):  # 위쪽 행 왼쪽으로 이동
                self.arr[layer][i] = self.arr[layer][i + 1]

            for i in range(layer, y):  # 오른쪽 열 위로 이동
                self.arr[i][x] = self.arr[i + 1][x]

            for i in range(x, layer, -1):  # 아래쪽 행 오른쪽으로 이동
                self.arr[y][i] = self.arr[y][i - 1]

            for i in range(y, layer, -1):  # 왼쪽 열 아래로 이동
                self.arr[i][layer] = self.arr[i - 1][layer]

            self.arr[layer + 1][layer] = top_left  # 저장한 초기 값을 사용

    def solve(self):
        for layer in range(min(self.n, self.m) // 2):
            self.rotate(layer)

        for row in self.arr:
            print(*row)


problem = Main()
problem.solve()
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.arr = [list(input()) for _ in range(self.n)]
        self.answer = 1

    def solve(self):
        for y in range(self.n):  # 시간 제한 2초, 50 x 50 x 50이므로 완탐 가능
            for x in range(self.m):
                for i in range(min(self.n, self.m)):  # 위에서 아래 방향으로 범위 확장, 정사각형이므로 최소 길이에 맞춤
                    my, mx = y + i, x + i
                    if my < self.n and mx < self.m:  # 순차적으로 확장시킨 범위가 벗어나지 않았고
                        if self.arr[y][x] == self.arr[my][x] == self.arr[y][mx] == self.arr[my][mx]:  # 네 꼭짓점이 같다면
                            self.answer = max(self.answer, (i + 1)**2)  # 크기 갱신

        print(self.answer)


problem = Main()
problem.solve()
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.tc = int(input())
        self.directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

    def solve(self):
        for _ in range(self.tc):
            l = int(input())
            knight = tuple(map(int, input().split()))
            target = tuple(map(int, input().split()))
            dq = deque([])
            visited = [[False] * l for _ in range(l)]
            visited[knight[0]][knight[1]] = True
            dq.append((knight[0], knight[1], 0))

            while dq:
                y, x, step = dq.popleft()
                if (y, x) == target:
                    print(step)
                    break

                for dy, dx in self.directions:
                    my, mx = y + dy, x + dx
                    if 0 <= my < l and 0 <= mx < l and not visited[my][mx]:
                        visited[my][mx] = True
                        dq.append((my, mx, step + 1))


problem = Main()
problem.solve()

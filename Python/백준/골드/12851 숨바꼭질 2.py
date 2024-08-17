from collections import deque


class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())

    def solve(self):
        cnt = 0
        time = [0] * 100001
        dq = deque([self.n])

        while dq:
            x = dq.popleft()
            if x == self.k:
                cnt += 1
                continue

            for pos in [x - 1, x + 1, 2 * x]:
                if pos < 0 or 100000 < pos:
                    continue
                if not time[pos] or time[pos] == time[x] + 1:  # 방문 안 했거나 다음에 방문할 수 있다면(=특정 위치 재방문)
                    time[pos] = time[x] + 1  # 다음 위치의 시간은 현재까지 소요된 시간 + 1
                    dq.append(pos)

        print(time[self.k])
        print(cnt)


problem = Main()
problem.solve()





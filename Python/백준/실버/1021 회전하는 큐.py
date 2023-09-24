from collections import deque

class main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.indices = [i-1 for i in map(int, input().split())]
        self.answer = 0

    def solve(self):
        dq = deque(list(range(self.n)))
        i = 0

        while i < self.m:
            if self.indices[i] == dq[0]:
                dq.popleft()
                i += 1
            else:
                if dq.index(self.indices[i]) <= len(dq) // 2:
                    dq.rotate(-1)
                else:
                    dq.rotate()
                self.answer += 1
        print(self.answer)

main = main().solve()
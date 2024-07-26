import sys
from collections import deque
input = lambda: sys.stdin.readline()


class Main:
    def __init__(self):
        self.n, self.q, self.k = map(int, input().split())
        self.cmd = [tuple(map(int, input().split())) for _ in range(self.q)]

    def solve(self):
        last_order = max([i if c[0] == 1 else 0 for i, c in enumerate(self.cmd)])  # 마지막 정렬이 일어난 위치
        flag = sum([c[0] == 2 for c in self.cmd[:last_order]]) % 2 != 0  # 마지막 정렬이 이뤄지기 전까지 뒤집기 여부
        dq = deque([c[1] for c in self.cmd[:last_order] if c[0] == 0])  # 맨 앞에 추가 = 가장 먼저 처리
        if last_order != 0:
            dq = deque(sorted(dq))  # 정렬 후, 고유번호 값이 낮은 업무가 스케줄러 앞에 배치 = 앞에 배치된 업무 먼처 처리
            flag = False  # 정렬 이후 업무 처리 기준이 새롭게 정의되었으므로 기존의 처리 순서 초기화

        for c in self.cmd[last_order:]:
            if c[0] == 0:
                dq.appendleft(c[1]) if not flag else dq.append((c[1]))
            elif c[0] == 2:
                flag = not flag

        print(dq[self.k-1] if not flag else dq[-self.k])


problem = Main()
problem.solve()
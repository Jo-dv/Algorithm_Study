from collections import deque
from itertools import permutations


class Main:
    def __init__(self):
        self.n = int(input())
        self.hp = list(map(int, input().split()))

    def solve(self):
        scv = tuple(sorted(self.hp, reverse=True)) + tuple(0 for _ in range(3 - len(self.hp)))
        visited = set(scv)
        dq = deque([(*scv, 0)])
        attack_set = list(permutations([9, 3, 1]))

        while dq:
            scv1, scv2, scv3, attack_cnt = dq.popleft()
            if scv1 == scv2 == scv3 == 0:
                print(attack_cnt)
                return

            for atk1, atk2, atk3 in attack_set:
                damaged_scv1, damaged_scv2, damaged_scv3 = max(0, scv1 - atk1), max(0, scv2 - atk2), max(0, scv3 - atk3)
                damaged_scv = tuple(sorted((damaged_scv1, damaged_scv2, damaged_scv3), reverse=True))  # 체력 많은 순 처리

                if damaged_scv not in visited:
                    visited.add(damaged_scv)
                    dq.append((*damaged_scv, attack_cnt + 1))

        print(-1)


problem = Main()
problem.solve()
from collections import deque

class Main:
    def __init__(self):
        self.t = int(input())

    def solve(self):
        for _ in range(self.t):
            answer = 0
            w, n = map(int, input().split())  # w만큼 쓰레기 적재 가능
            info = deque([])
            for _ in range(n):
                xi, wi = map(int, input().split())
                info.append((xi, wi))  # xi: 거리, wi: 쓰레기의 양

            cap = w  # 현재 수용량
            last = info[-1]

            while info:
                if cap > info[0][1]:  # 현재 쓰레기가 수용량보다 적다면
                    cap -= info[0][1]
                    info.popleft()
                elif cap == info[0][1]:  # 현재 쓰레기를 담았을 때 다 찬다면
                    cap = w
                    answer += info[0][0] * 2
                    info.popleft()
                else:  # 수용량보다 쓰레기가 더 많다면
                    answer += info[0][0] * 2
                    cap = w

            if cap < w:  # 마지막에 도달했는데 쓰레기가 남았다면
                answer += last[0] * 2

            print(answer)


problem = Main()
problem.solve()

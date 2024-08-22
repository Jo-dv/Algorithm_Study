from collections import deque
from typing import List


class Main:
    def __init__(self):
        self.gears = [list(input()) for _ in range(4)]
        self.k = int(input())
        self.cmd = [list(map(int, input().split())) for _ in range(self.k)]
        self.answer = 0

    def rotate(self, start, step, d, head, tail):  # 검사하는 톱니에서 다른 톱니와 맞닿은 부분이 head, 다른 톱니는 tail
        self.gears: List[deque]
        previous = self.gears[start][tail]  # 입력받은 기어 기준으로 앞뒤 기어들을 검사

        for i in range(start + step, 4 if step == 1 else -1, step):  # 파라미터에 따라 앞 혹은 뒤로 검사
            if previous != self.gears[i][head]:  # 왼쪽 검사는 head: 2, 오른쪽 검사는 head: 6
                previous = self.gears[i][tail]  # 현재 톱니의 tail이 다음 톱니에 맞닿는 부분이기 때문에 회전하기 전에 미리 저장
                d *= -1  # 이전 톱니 회전 방향과 반대
                self.gears[i].rotate(d)  # 방향에 맞춰 회전
            else:
                break  # 일치한다는 것은 회전시킬 필요가 없다는 것이므로 다른 톱니들도 회전할 필요가 없음

    def calculate(self):
        points = {0: 1, 1: 2, 2: 4, 3: 8}
        for i, gear in enumerate(self.gears):
            if gear[0] == '1':  # 12시 방향의 톱니가 S라면
                self.answer += points[i]  # 기어에 맞춰 점수 갱신

    def solve(self):
        self.gears: deque
        for i in range(4):  # 회전 로직을 구현하기 위해 입력받은 각 리스트를 deque 자료구조로 변경
            self.gears[i] = deque(self.gears[i])

        for i in range(self.k):  # 편의를 위해 인덱스 보정
            self.cmd[i][0] -= 1

        for gear, direction in self.cmd:
            self.rotate(gear, 1, direction, 6, 2)  # 현재 기어 기준 우측 기어들 검사
            self.rotate(gear, -1, direction, 2, 6)  # 현재 기어 기준 좌측 기어들 검사
            self.gears[gear].rotate(direction)  # 각 기어들은 기어가 회전하기 전 상태에 영향을 받기 때문에, 모든 액션이 끝나고 회전
        self.calculate()  # 점수 계산
        print(self.answer)


problem = Main()
problem.solve()

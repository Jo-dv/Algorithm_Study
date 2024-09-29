import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.data = input()
        self.m = int(input())
        self.cmd = [input().split() for _ in range(self.m)]

    def solve(self):
        left_stack = list(self.data)  # 커서 왼쪽에 있는 문자들
        right_stack = []  # 커서 오른쪽에 있는 문자들

        for c in self.cmd:
            if c[0] == 'L':
                if left_stack:
                    right_stack.append(left_stack.pop())  # 왼쪽에서 하나를 빼서 오른쪽에 추가
            elif c[0] == 'D':
                if right_stack:
                    left_stack.append(right_stack.pop())  # 오른쪽에서 하나를 빼서 왼쪽에 추가
            elif c[0] == 'B':
                if left_stack:
                    left_stack.pop()  # 왼쪽에서 하나를 삭제
            else:
                _, s = c
                left_stack.append(s)  # 왼쪽에 문자를 추가

        # 최종 결과 출력
        print(''.join(left_stack + right_stack[::-1]))  # 오른쪽 스택은 역순으로 합침


problem = Main()
problem.solve()

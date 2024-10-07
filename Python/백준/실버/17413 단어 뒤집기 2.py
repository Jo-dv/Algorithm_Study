from collections import deque

class Main:
    def __init__(self):
        self.s = input()
        self.answer = ""

    def solve(self):
        dq = deque([])
        for i in self.s:
            if i == '<':  # 문자들이 나오다가 여는 꺽쇠가 나온 경우
                while dq:
                    self.answer += dq.pop()
            dq.append(i)
            if dq:
                if dq[-1] == '>':  # 닫는 꺽쇠가 나온 경우 정방향 처리
                    while dq:
                        self.answer += dq.popleft()
                elif dq[0] != '<' and dq[-1] == ' ':
                    dq.pop()
                    while dq:
                        self.answer += dq.pop()
                    self.answer += i

        while dq:
            self.answer += dq.pop()

        print(self.answer)


problem = Main()
problem.solve()
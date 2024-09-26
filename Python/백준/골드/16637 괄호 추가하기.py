class Main:
    def __init__(self):
        self.n = int(input())
        self.exp = input()
        self.answer = -2**31

    @staticmethod
    def calculate(val1, op, val2):
        return (val1 + val2) if op == '+' else (val1 - val2) if op == '-' else (val1 * val2)

    def search(self, result, idx):
        if idx == self.n:
            self.answer = max(self.answer, result)
            return

        next_result = self.calculate(result, self.exp[idx], int(self.exp[idx + 1]))  # 괄호 없음
        self.search(next_result, idx + 2)  # 다음 연산자로

        if idx + 2 < self.n:  # 다음 연산자가 마지막이 아니라면 괄호 추가
            bracket = self.calculate(int(self.exp[idx + 1]), self.exp[idx + 2], int(self.exp[idx + 3]))
            next_result = self.calculate(result, self.exp[idx], bracket)
            self.search(next_result, idx + 4)

    def solve(self):
        self.search(int(self.exp[0]), 1)  # 첫 연산자와 연산자 왼쪽 값
        print(self.answer)


problem = Main()
problem.solve()

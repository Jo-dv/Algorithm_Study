class Main:
    def __init__(self):
        self.board = input()
        self.answer = []

    def solve(self):
        parts = self.board.split('.')  # . 기준으로 나누기

        for part in parts:
            if not part:
                self.answer.append('')
                continue

            n = len(part)
            if n % 2 != 0:  # 폴리오미노는 모두 짝수
                print(-1)
                return

            self.answer.append('AAAA' * (n // 4) + 'BB' * ((n % 4) // 2))  # 가장 긴 폴리오미노 설치, 그 다음 짧은 폴리오미노

        print('.'.join(self.answer))  # . 기준으로 합치기


problem = Main()
problem.solve()
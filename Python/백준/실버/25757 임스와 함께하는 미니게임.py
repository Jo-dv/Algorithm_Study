import sys
input = lambda: sys.stdin.readline()


class Main:
    def __init__(self):
        self.n, self.g_type = input().split()
        self.players = set(input() for _ in range(int(self.n)))  # 한 번 같이 한 사람은 다시 게임을 하지 않으므로 중복처리

    def solve(self):
        game = {'Y': 1, 'F': 2, 'O': 3}  # 임스를 제외하고 게임을 진행하기 위해 필요한 인원
        print(len(self.players) // game[self.g_type])  # 추려진 인원의 수를 바탕으로 진행하려는 게임을 나누면 가능한 게임 계산 가능


problem = Main()
problem.solve()
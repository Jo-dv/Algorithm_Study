import random
from math import exp


class Main:
    def __init__(self):
        self.n = int(input())
        self.board = [list(input().strip()) for _ in range(self.n)]
        self.T = 2  # 초기 온도
        self.cooling_rate = 0.99999
        self.max_iterations = 10000

    def flip_coin(self, coin):
        return 'H' if coin == 'T' else 'T'

    def count_tails(self, board, pr=None):  # 현재 행에서 뒤집거나 유지해서 만들 수 있는 T의 수 계산
        tails_count = 0
        # if pr < 0.5:  # 각 행에서 비교(열 방향 뒤집기)
        for r in range(self.n):  # 행을 검사하는 이유를 특정 열을 뒤집었을 때, 각 행들이 간섭받으므로
            tails_count += min(board[r].count('T'), self.n - board[r].count('T'))  # T의 수, H의 수
        # else:  # 각 열에서 비교(행 방향 뒤집기)
            # for c in range(self.n):
            #     col_tails = sum(1 for r in range(self.n) if board[r][c] == 'T')
            #     tails_count += min(col_tails, self.n - col_tails)
        return tails_count

    def generate_neighbor(self, current_board, pr=None):
        # 유전 알고리즘 특성상 다양성 확보를 위해 행, 열 다 생성했지만, 고정하는 것이 효과적
        # n x n의 크기라 행과 열을 함께 처리하면 원상복구되는 데이터가 있어서 그런 것으로 판단
        idx = random.randint(0, self.n - 1)
        new_board = [r[:] for r in current_board]
        # if pr < 0.5:  # 열 방향 뒤집기
        for row in new_board:
            row[idx] = self.flip_coin(row[idx])
        # else:  # 행 방향 뒤집기
        #     for i in range(self.n):
        #         new_board[idx][i] = self.flip_coin(new_board[idx][i])

        return new_board

    def simulated_annealing(self):
        current_board = self.board
        current_energy = self.n**2
        best_energy = current_energy

        for _ in range(self.max_iterations):
            # pr = random.randint(0, 1)
            new_board = self.generate_neighbor(current_board)
            next_energy = self.count_tails(new_board)
            delta_E = next_energy - current_energy

            if delta_E < 0 or random.random() < exp(-delta_E / self.T):
                current_board = new_board
                current_energy = next_energy

            best_energy = min(best_energy, current_energy)

            self.T *= self.cooling_rate

        return best_energy

    def solve(self):
        answer = self.simulated_annealing()
        print(answer)


problem = Main()
problem.solve()
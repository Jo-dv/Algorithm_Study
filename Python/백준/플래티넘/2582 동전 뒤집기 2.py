import random
from math import exp


class Main:
    def __init__(self):
        self.n = int(input())
        self.board = [list(input().strip()) for _ in range(self.n)]
        self.T = 1 * 2  # 초기 온도
        self.cooling_rate = 0.9999
        self.max_iterations = 5000

    def count_tails(self, board):
        tails_count = 0
        for r in range(self.n):
            tails_count += min(board[r].count('T'), self.n - board[r].count('T'))
        return tails_count

    def generate_neighbor(self, current_board):
        col_to_flip = random.randint(0, self.n - 1)  # 랜덤하게 뒤집을 열을 선택

        new_board = [r[:] for r in current_board]  # 현재 보드를 복사

        for r in range(self.n):  # 선택한 열을 뒤집음
            new_board[r][col_to_flip] = 'H' if new_board[r][col_to_flip] == 'T' else 'T'

        return new_board  # 새로운 보드 반환

    def simulated_annealing(self):
        current_board = self.board
        current_energy = self.count_tails(current_board)
        best_energy = current_energy

        for _ in range(self.max_iterations):
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
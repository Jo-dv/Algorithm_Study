import random
import math


class Main:
    def __init__(self):
        self.n = int(input())
        self.board = [list(input().strip()) for _ in range(self.n)]
        self.T = 2.5  # 초기 온도
        self.cooling_rate = 0.9999
        self.max_iterations = 5000

    def flip_coin(self, coin):
        return 'H' if coin == 'T' else 'T'

    def count_tails(self, board):
        tails_count = 0
        for r in range(self.n):
            tails_count += min(board[r].count('T'), self.n - board[r].count('T'))
        return tails_count

    def generate_neighbor(self, current_board):
        # 한 번의 행동으로 하나의 행 또는 열을 뒤집음
        if random.random() < 0.5:
            # 행을 뒤집음
            r = random.randint(0, self.n - 1)
            new_board = [r[:] for r in current_board]
            new_board[r] = [self.flip_coin(coin) for coin in new_board[r]]
        else:
            # 열을 뒤집음
            c = random.randint(0, self.n - 1)
            new_board = [r[:] for r in current_board]
            for row in new_board:
                row[c] = self.flip_coin(row[c])

        return new_board

    def simulated_annealing(self):
        current_board = self.board
        current_energy = self.count_tails(current_board)
        best_energy = current_energy

        for _ in range(self.max_iterations):
            new_board = self.generate_neighbor(current_board)
            next_energy = self.count_tails(new_board)
            delta_E = next_energy - current_energy

            # 수용 확률을 계산하여 현재 상태를 업데이트
            if delta_E < 0 or random.random() < math.exp(-delta_E / self.T):
                current_board = new_board
                current_energy = next_energy

            best_energy = min(best_energy, current_energy)

            # 온도를 감소시킴
            self.T *= self.cooling_rate

        return best_energy

    def solve(self):
        answer = self.simulated_annealing()
        print(answer)

problem = Main()
problem.solve()
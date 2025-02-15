class Main:
    def __init__(self):
        self.test_case = None

    def check(self, x_cnt, o_cnt):
        board = [list(self.test_case[i:i + 3]) for i in range(0, 9, 3)]
        x_wins, o_wins = False, False  # X와 O의 승리 여부 체크

        # 가로 체크
        for i in range(3):
            if board[i][0] != "." and board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] == "X":
                    x_wins = True
                if board[i][0] == "O":
                    o_wins = True

        # 세로 체크
        for i in range(3):
            if board[0][i] != "." and board[0][i] == board[1][i] == board[2][i]:
                if board[0][i] == "X":
                    x_wins = True
                if board[0][i] == "O":
                    o_wins = True

        # 대각선 체크
        if board[0][0] != "." and board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == "X":
                x_wins = True
            if board[0][0] == "O":
                o_wins = True

        if board[0][2] != "." and board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == "X":
                x_wins = True
            if board[0][2] == "O":
                o_wins = True

        # 동시에 X와 O가 승리하면 invalid -> 고려하지 못했던 예외케이스 1
        if x_wins and o_wins:
            return False

        # X가 이긴 경우 X가 한 턴 더 많아야 함
        if x_wins and x_cnt - o_cnt == 1:
            return True

        # O가 이긴 경우 X와 O 개수가 같아야 함
        if o_wins and x_cnt == o_cnt:
            return True

        # 보드가 꽉 찬 경우 (X 5개, O 4개)  -> 고려하지 못했던 예외케이스 2: 보드가 꽉찼을 때 O가 이기는 경우를 고려하지 못함
        if not o_wins and x_cnt == 5 and o_cnt == 4:
            return True

        return False

    def solve(self):
        while True:
            self.test_case = input()
            if self.test_case == "end":
                return

            x_cnt = self.test_case.count("X")
            o_cnt = self.test_case.count("O")

            if o_cnt > x_cnt or (x_cnt < 3 and o_cnt < 3) or (x_cnt - o_cnt > 1):
                print("invalid")
                continue

            if self.check(x_cnt, o_cnt):
                print("valid")
            else:
                print("invalid")


problem = Main()
problem.solve()

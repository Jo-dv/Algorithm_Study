class Main:
    def __init__(self):
        self.board = [list(input()) for _ in range(9)]
        self.row_masks = [0] * 9  # bitwise 연산을 위한 리스트
        self.col_masks = [0] * 9
        self.box_masks = [0] * 9

    def search_zero(self):  # 보드에서 값이 0인 위치를 탐색 후, 저장
        return [(y, x) for y in range(9) for x in range(9) if self.board[y][x] == "0"]

    def init_masks(self):
        for y in range(9):
            for x in range(9):
                if self.board[y][x] != "0":
                    num = int(self.board[y][x])
                    mask = 1 << num  # 주어진 보드의 값을 비트로 변환
                    self.row_masks[y] |= mask
                    self.col_masks[x] |= mask
                    self.box_masks[(y // 3) * 3 + (x // 3)] |= mask  # 3x3 박스의 인덱스 표현 0 ~ 8

    def is_valid(self, y, x, num):  # 숫자 삽입을 위한 보드의 유효성 검사
        mask = 1 << num
        if (self.row_masks[y] & mask) != 0:  # 비트에 대한 & 연산은 두 비트 모두 동일할 경우 1울 만들어 냄
            return False
        if (self.col_masks[x] & mask) != 0:
            return False
        if (self.box_masks[(y // 3) * 3 + (x // 3)] & mask) != 0:
            return False
        return True

    def place_num(self, y, x, num):
        mask = 1 << num
        self.board[y][x] = str(num)
        self.row_masks[y] |= mask
        self.col_masks[x] |= mask
        self.box_masks[(y // 3) * 3 + (x // 3)] |= mask

    def remove_num(self, y, x, num):
        mask = ~(1 << num)
        self.board[y][x] = "0"
        self.row_masks[y] &= mask
        self.col_masks[x] &= mask
        self.box_masks[(y // 3) * 3 + (x // 3)] &= mask

    def finish_sudoku(self, zero_pos, pos):
        if pos == len(zero_pos):
            for row in self.board:
                print("".join(row))
            return True  # 여러 정답이 나올 수 있기 때문에 최초의 정답이 만들어지면 메서드 종료를 위해 True 반환

        y, x = zero_pos[pos]
        for num in range(1, 10):
            if self.is_valid(y, x, num):  # 현재 위치에 숫자를 두는 것이 유효한 선택이라면
                self.place_num(y, x, num)  # 숫자 삽입
                if self.finish_sudoku(zero_pos, pos + 1):  # 최초의 정답이 만들어지면 메서드 종료
                    return True  # dfs 방식이므로 이전 호출에 대해서도 결과를 알려줘야 함
                self.remove_num(y, x, num)

        return False

    def solve(self):
        self.init_masks()
        zero_pos = self.search_zero()
        self.finish_sudoku(zero_pos, 0)


problem = Main()
problem.solve()

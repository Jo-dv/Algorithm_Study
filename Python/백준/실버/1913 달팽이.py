class Main:
    def __init__(self):
        self.n = int(input())
        self.target = int(input())

    def search(self, board):
        for y in range(self.n):
            for x in range(self.n):
                if board[y][x] == self.target:
                    print(y + 1, x + 1)
                    return

    def solve(self):
        board = [[1] * self.n for _ in range(self.n)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        y = x = self.n // 2

        max_distance = 1
        current_distance = 0
        cnt = 0
        d = 0

        while True:
            dy, dx = directions[d]
            my, mx = y + dy, x + dx
            if (my, mx) == (-1, 0):
                break
            board[my][mx] += board[y][x]
            y, x = my, mx

            current_distance += 1
            if current_distance == max_distance:
                current_distance = 0
                d = (d + 1) % 4
                cnt += 1
                if cnt == 2:
                    max_distance += 1
                    cnt = 0

        for i in board:
            print(*i)

        self.search(board)


problem = Main()
problem.solve()



class Main:
    def __init__(self):
        self.n = int(input())
        self.board = [input() for _ in range(self.n)]
        self.heart = [0, 0]
        self.body = [0, 0, 0, 0, 0]

    def find_heart(self):
        cnt = 0
        for i, cookie in enumerate(self.board, 1):
            pos = cookie.find('*')
            if pos == -1:
                continue
            cnt += 1
            if cnt == 1:
                self.heart[1] = pos + 1
            if cnt == 2:
                self.heart[0] = i
                break

        return

    def measure_arms(self):
        left_arm, right_arm = 0, 0
        heart_y = self.heart[0] - 1
        heart_x = self.heart[1] - 1
        for i in range(heart_x - 1, -1, -1):
            if self.board[heart_y][i] == '*':
                left_arm += 1

        for i in range(heart_x + 1, self.n):
            if self.board[heart_y][i] == '*':
                right_arm += 1

        self.body[0] = left_arm
        self.body[1] = right_arm

    def measure_waist(self):
        waist = 0
        heart_y = self.heart[0] - 1
        heart_x = self.heart[1] - 1
        for i in range(heart_y + 1, self.n):
            if self.board[i][heart_x] == '*':
                waist += 1

        self.body[2] = waist
        return heart_y + waist

    def measure_legs(self, waist_pos):
        left_leg, right_leg = 0, 0
        heart_x = self.heart[1] - 1
        for i in range(waist_pos + 1, self.n):
            if self.board[i][heart_x - 1] == '*':
                left_leg += 1
            if self.board[i][heart_x + 1] == '*':
                right_leg += 1

        self.body[3] = left_leg
        self.body[4] = right_leg

    def solve(self):
        self.find_heart()
        self.measure_arms()
        waist_pos = self.measure_waist()
        self.measure_legs(waist_pos)

        print(*self.heart)
        print(*self.body)


problem = Main()
problem.solve()
class Main:
    def __init__(self):
        self.s = input()

    def solve(self):
        one = self.s.split('0')
        zero = self.s.split('1')
        one_count = len(one) - one.count('')  # 1의 개수
        zero_count = len(zero) - zero.count('')  # 1의 개수

        if one_count == 0 or zero_count == 0:
            print(0)
        else:
            print(one_count if one_count < zero_count else zero_count)


problem = Main()
problem.solve()
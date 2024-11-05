class Main:
    def __init__(self):
        self.k = int(input())
        self.sign = list(input().split())
        self.answer = ["", ""]

    def is_valid(self, prev, curr, sign):
        return (sign == '<' and prev < curr) or (sign == '>' and prev > curr)

    def search(self, depth, result, used):
        if depth == self.k + 1:
            num = ''.join(map(str, result))
            if not self.answer[0] or num > self.answer[0]:
                self.answer[0] = num
            if not self.answer[1] or num < self.answer[1]:
                self.answer[1] = num
            return

        for i in range(10):
            if not used[i]:
                if depth == 0 or self.is_valid(result[-1], i, self.sign[depth - 1]):
                    used[i] = True
                    self.search(depth + 1, result + [i], used)
                    used[i] = False

    def solve(self):
        used = [False] * 10
        self.search(0, [], used)
        print(self.answer[0])
        print(self.answer[1])


problem = Main()
problem.solve()

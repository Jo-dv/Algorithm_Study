import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.cmd = [input() for _ in range(self.n)]
        self.answer = set()

    def solve(self):
        chain = dict()
        babas = set()
        for i in self.cmd:
            p, c, q = i.split()
            if p == "Baba":  # Baba로 만들 수 있는게 여러개일 수 있음
                babas.add(q)
                self.answer.add(q)
            else:
                chain[p] = q

        self.answer |= babas

        for cur in babas:  # 준비된 baba들로 시작
            while cur in chain:  # 현재 사물로 만들 수 있는게 있을 때까지
                self.answer.add(cur)
                cur = chain[cur]
            self.answer.add(cur)  # 마지막 만들어진 사물은 추가가 반복문에서 안 되므로

        self.answer = sorted(list(self.answer))

        for i in self.answer:
            print(i)


problem = Main()
problem.solve()
from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.words = [input() for _ in range(self.n)]

    def solve(self):
        note = defaultdict(int)

        for word in self.words:
            if len(word) < self.m:
                continue
            note[word] += 1

        note = list(note.items())
        note.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

        for word, _ in note:
            print(word)


problem = Main()
problem.solve()

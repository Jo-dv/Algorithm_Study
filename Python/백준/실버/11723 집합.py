import sys

m = int(input())
ansewr = []
## 울 재 ~~~
class sol:
    def __init__(self):
        self.s = list()

    def add(self, x):
        if x not in self.s:
            self.s.append(x)

    def remove(self, x):
        if x in self.s:
            self.s.remove(x)

    def check(self, x):
        ansewr.append('1' if x in self.s else '0')

    def toggle(self, x):
        self.s.remove(x) if x in self.s else self.s.append(x)

    def all(self):
        self.s = [str(i) for i in range(1, 21)]

    def empty(self):
        self.s = []

problem = sol()

for _ in range(m):
    op = sys.stdin.readline().split()

    if op[0] == 'add' and op[1] not in problem.s:
        problem.add(op[1])
    elif op[0] == 'remove' and op[1] in problem.s:
        problem.remove(op[1])
    elif op[0] == 'check':
        problem.check(op[1])
    elif op[0] == 'toggle':
        problem.toggle(op[1])
    elif op[0] == 'all':
        problem.all()
    else:
        problem.empty()

for i in ansewr:
    print(i)
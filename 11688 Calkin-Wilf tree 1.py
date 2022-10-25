class Tree:
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b
        self.Node = [a, b]
        self.left = None
        self.right = None

T = int(input())

for i in range(1, T+1):
    c = input()
    t = Tree()  # tree 객체 생성

    for j in c:
        if j == "L":
            t.left = Tree(t.a, t.a+t.b)  # a/a+b
            t = t.left  # tree를 새로 생긴 왼쪽 자식으로 갱신
        else:
            t.right = Tree(t.a+t.b, t.b)  # a+b/b
            t = t.right  # tree를 새로 생긴 오른쪽 자식으로 갱신

    print(f'#{i}', *t.Node)
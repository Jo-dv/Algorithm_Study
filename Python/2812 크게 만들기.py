class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.num = input()
        self.stack = []

    def solve(self):
        for i in range(self.n):
            while self.k and self.stack and self.stack[-1] < self.num[i]:  # 문자열이라도 단일 숫자는 순서로 크기를 비교
                self.stack.pop()
                self.k -= 1

            self.stack.append(self.num[i])

        if self.k:  # 무조건적으로 k개 만큼 수를 제거해야 하므로 k가 남아있다면 처리해줘야 함
            self.stack = self.stack[:-self.k]
            # 위 로직으로 처리하면 완전하진 않지만 숫자가 내림차순의 형태거나 모든 숫자들이 동일하면 값을 제거할 수 없음
            # 5 3 11111
            # 6 4 765462

        print("".join(self.stack))


problem = Main()
problem.solve()
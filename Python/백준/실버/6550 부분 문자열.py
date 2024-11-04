class Main:
    def __init__(self):
        self.test_case = []

    def solve(self):
        while True:
            try:
                case = input().split()
                if not case:
                    break
            except EOFError:
                break
            self.test_case.append(case)

        for case in self.test_case:
            s, t = case
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:  # 문자열이 제거된 상태에서 그대로 재조합이니 순차적으로 탐색
                    i += 1
                    j += 1
                else:
                    j += 1

            print("Yes" if i >= len(s) else "No")


problem = Main()
problem.solve()
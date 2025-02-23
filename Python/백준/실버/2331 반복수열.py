class Main:
    def __init__(self):
        self.a, self.p = input().split()
        self.answer = 0

    def solve(self):
        d = [self.a]
        visited = {int(self.a): 1}
        self.p = int(self.p)

        while True:
            new_num = sum([int(i)**self.p for i in d[-1]])
            if new_num not in visited:
                visited[new_num] = 1
            else:
                visited[new_num] += 1
                if visited[new_num] >= 2:  # 수열이 발생하는 순간 이미 나온 수가 다시 발생할 것이므로
                    break

            d.append(str(new_num))

        for value in visited.values():
            if value == 1:
                self.answer += 1
            else:
                break

        print(self.answer)


problem = Main()
problem.solve()
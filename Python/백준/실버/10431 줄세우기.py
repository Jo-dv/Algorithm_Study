class Main:
    def __init__(self):
        self.p = int(input())

    def solve(self):
        answer = []

        for _ in range(self.p):
            test_case = list(map(int, input().split()))
            t, height = test_case[0], test_case[1:]
            step = 0
            for i in range(19, 0, -1):  # 버블정렬 구현 문제
                for j in range(i):
                    if height[j] > height[j + 1]:
                        height[j], height[j + 1] = height[j + 1], height[j]
                        step += 1

            answer.append(step)

        for i, step in enumerate(answer, 1):
            print(f'{i} {step}')


problem = Main()
problem.solve()
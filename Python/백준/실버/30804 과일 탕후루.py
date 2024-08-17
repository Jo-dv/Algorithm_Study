from collections import defaultdict


class Main:
    def __init__(self):
        self.n = int(input())
        self.tanghulu = list(map(int, input().split()))

    def solve(self):
        fruits = defaultdict(int)
        left = 0
        answer = 0

        for right in range(self.n):
            fruit = self.tanghulu[right]
            fruits[fruit] += 1  # 과일 추가

            while len(fruits) > 2:  # 과일의 종류가 2개를 넘는다면
                fruit = self.tanghulu[left]
                fruits[fruit] -= 1  # 왼쪽에서부터 과일 제거
                if fruits[fruit] == 0:
                    fruits.pop(fruit)  # 탕후루에서 과일이 완전히 제거되었으므로 종류에서 제거
                left += 1

            answer = max(answer, right - left + 1)

        print(answer)


problem = Main()
problem.solve()
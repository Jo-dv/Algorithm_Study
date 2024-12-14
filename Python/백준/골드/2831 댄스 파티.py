class Main:
    def __init__(self):
        self.n = int(input())
        self.men = list(map(int, input().split()))
        self.women = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        self.men.sort()
        self.women.sort()
        low, high = 0, self.n - 1

        while low < self.n and 0 <= high:
            man = abs(self.men[low])
            woman = abs(self.women[high])
            if self.men[low] > 0 and self.women[high] < 0:
                if man < woman:
                    low += 1
                    high -= 1
                    self.answer += 1
                else:  # 이미 남자가 여자보다 같거나 큰 경우이므로, 여자만 낮춰주면 같다라는 조건을 제거할 수 있음
                    high -= 1
            elif self.men[low] < 0 and self.women[high] > 0:
                if man > woman:
                    low += 1
                    high -= 1
                    self.answer += 1
                else:  # 남자가 여자보다 같거나 작은 상황에서 남자를 올리면 양수, 양수의 상황이 발생
                    high -= 1
            elif self.men[low] < 0 and self.women[high] < 0:  # 한 쪽을 양수로 맞춰야 함
                low += 1
            elif 0 < self.men[low] and 0 < self.women[high]:  # 한 쪽을 음수로 맞춰야 함
                high -= 1

        print(self.answer)


problem = Main()
problem.solve()
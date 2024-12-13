class Main:
    def __init__(self):
        self.n = int(input())
        self.a = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        self.a.sort()
        for i in range(self.n):
            target = self.a[i]
            low, high = 0, self.n - 1

            while low < high:
                num = self.a[low] + self.a[high]
                if num == target:
                    if low == i:
                        low += 1
                    elif high == i:
                        high -= 1
                    else:
                        self.answer += 1
                        break
                elif num < target:
                    low += 1
                else:
                    high -= 1

        print(self.answer)


problem = Main()
problem.solve()
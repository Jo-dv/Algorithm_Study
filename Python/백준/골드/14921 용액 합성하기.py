class Main:
    def __init__(self):
        self.n = int(input())
        self.arr = list(map(int, input().split()))
        self.answer = float('inf')

    def solve(self):
        low, high = 0, self.n - 1

        while low < high:
            temp = self.arr[low] + self.arr[high]
            if abs(temp) < abs(self.answer):
                self.answer = temp
            if temp <= 0:  # 특정 조합의 합이 0이 만들어졌을 때에도 포인터는 움직여야 반복문을 종료할 수 있으므로 -> 반대의 경우도 가능
                low += 1
            else:
                high -= 1

        print(self.answer)


problem = Main()
problem.solve()
class Main:
    def __init__(self):
        self.n = int(input())
        self.arr = list(map(int, input().split()))
        self.answer = 0

    def search(self, arr, energy):
        if len(arr) == 2:
            self.answer = max(self.answer, energy)
            return
        for i in range(1, len(arr) - 1):
            num = arr[i]
            energy += (arr[i - 1] * arr[i + 1])
            arr.pop(i)
            self.search(arr, energy)
            arr.insert(i, num)
            energy -= (arr[i - 1] * arr[i + 1])

    def solve(self):
        self.search(self.arr, 0)
        print(self.answer)


problem = Main()
problem.solve()
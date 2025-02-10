import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.t = int(input())

    def binary_search(self, note, target):
        low, high = 0, len(note) - 1

        while low <= high:
            mid = (low + high) // 2
            if note[mid] == target:
                return 1
            elif note[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return 0

    def solve(self):
        for _ in range(self.t):
            n = int(input())
            note_1 = list(map(int, input().split()))
            m = int(input())
            note_2 = list(map(int, input().split()))
            note_1.sort()

            for num in note_2:
                print(self.binary_search(note_1, num))


problem = Main()
problem.solve()

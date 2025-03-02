from collections import defaultdict


class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.nums = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        count = defaultdict(int)
        left = right = 0

        while right < self.n:
            if count[self.nums[right]] < self.k:
                count[self.nums[right]] += 1
                right += 1
            else:
                count[self.nums[left]] -= 1
                left += 1

            self.answer = max(self.answer, right - left)

        print(self.answer)


problem = Main()
problem.solve()

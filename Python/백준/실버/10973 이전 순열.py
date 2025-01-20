class Main:
    def __init__(self):
        self.n = int(input())
        self.nums = list(map(int, input().split()))

    def solve(self):
        nums = self.nums
        i = len(nums) - 2

        while i >= 0 and nums[i] <= nums[i + 1]:
            i -= 1

        if i == -1:
            print(-1)
        else:
            j = len(nums) - 1
            while nums[j] >= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

            nums[i + 1:] = reversed(nums[i + 1:])
            print(*nums)


problem = Main()
problem.solve()

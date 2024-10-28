class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        check = set(nums)
        answer = -1

        for i in range(len(nums) - 1, -1, -1):
            cnt = 0
            temp = nums[i]
            while True:
                if temp in check:
                    cnt += 1
                    temp = temp**0.5
                else:
                    break
                    
            answer = max(answer, cnt)

        return answer if answer > 1 else -1
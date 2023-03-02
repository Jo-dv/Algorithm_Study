from itertools import combinations

nums = [1,2,7,6,4]

def solution(nums):
    answer = 0
    n = sum(sorted(nums)[-3:])
    temp = [True for _ in range(n + 1)]

    for i in range(2, int(n ** 0.5) + 1):
        if temp[i]:
            j = 2
            while i * j <= n:
                temp[i * j] = False
                j += 1

    target = [i+2 for i, data in enumerate(temp[2:]) if data]

    for i in list(combinations(nums, 3)):
        if sum(i) in target:
            answer += 1

    return answer

print(solution(nums))
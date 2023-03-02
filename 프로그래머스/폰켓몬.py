import itertools

nums = [3,1,2,3]

'''
def solution(nums):
    if len(nums) // 2 < len(list(set(nums))):
        answer = list(itertools.permutations(set(nums), len(nums) // 2))
    else:
        answer = list(itertools.permutations(set(nums)))
    return len(answer[0])
'''

import itertools

def solution(nums):
    # 중복은 필요없으니 set을 통해 제거, set의 길이 = 데려갈 수 있는 모든 폰켓몬의 수
    # 데려갈 수 있는 폰켓몬의 수보다 set의 길이가 더 크면 데려갈 수 있는 폰켓몬의 수
    # 아니면 모든 폰켓몬
    if len(nums) // 2 == len(set(nums)):
        answer = len(nums) // 2
    elif len(nums) // 2 < len(set(nums)):
        answer = len(nums) // 2
    else:
        answer = len(set(nums))
    return answer

print(solution(nums))
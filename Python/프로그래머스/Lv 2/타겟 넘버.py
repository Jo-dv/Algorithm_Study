def solution(numbers, target):
    def dfs(target, idx, temp):
        if idx == len(numbers):  # 계산이 다 된 시점에선 idx+1 즉 idx=len이 됨
            return 1 if temp == target else 0  # 이때 결과가 target과 같으면 1, 아니면 0
        return dfs(target, idx+1, temp + numbers[idx]) + dfs(target, idx+1, temp - numbers[idx]) 
        # 더하고 뺐을 때 분기 결과에 대한 값을 합산

    return dfs(target, 0, 0)

numbers, target = [1, 1, 1, 1, 1], 3

print(solution(numbers, target))
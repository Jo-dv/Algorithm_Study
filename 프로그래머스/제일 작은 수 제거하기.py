arr = [4, 2, 3, 1]

def solution(arr):
    if len(arr) < 2:
        return [-1]
    arr.remove(min(arr))
    answer = arr
    return answer

print(solution(arr))
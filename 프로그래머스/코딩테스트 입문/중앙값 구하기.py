array = [1, 2, 7, 10, 11]

def solution(array):
    answer = sorted(array)[len(array)//2]
    return answer

print(solution(array))
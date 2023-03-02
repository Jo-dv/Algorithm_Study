arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    temp = None
    for i in arr:
        if i != temp:
            temp = i
            answer.append(temp)
        else:
            continue
    return answer

print(solution(arr))
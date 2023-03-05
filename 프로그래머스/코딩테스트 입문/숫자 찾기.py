num, k = 29183, 1

def solution(num, k):
    return str(num).index(str(k))+1 if str(k) in str(num) else -1

print(solution(num, k))
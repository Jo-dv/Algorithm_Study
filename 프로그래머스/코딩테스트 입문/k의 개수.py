i, j, k = 1, 13, 1

def solution(i, j, k):
    return sum([str(i).count(str(k)) for i in range(i, j+1)])

print(solution(i, j, k))
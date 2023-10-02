A = [1, 4, 2]
B = [5, 4, 4]

def solution(A,B):
    answer = 0
    for i, j in zip(sorted(A), sorted(B, reverse=True)):
        answer += i * j

    return answer

print(solution(A, B))
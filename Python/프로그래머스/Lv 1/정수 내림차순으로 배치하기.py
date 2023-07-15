n = 118372

def solution(n):
    answer = ''
    n = [int(i) for i in str(n)]
    n.sort(reverse=True)
    for i in n:
        answer += str(i)
    return int(answer)

print(solution(n))
n = 3

def solution(n):
    answer = []
    def hanoi(n, f, v, t):
        if n == 1:
            answer.append([f, t])
        else:
            hanoi(n-1, f, t, v)
            answer.append([f, t])
            hanoi(n-1, v, f, t)

    hanoi(n, 1, 2, 3)
    return answer

print(solution(n))


n = 4

def solution(n):
    global answer
    answer = 0
    col = [-1] * n

    def queens(i, n):
        global answer
        promising = True
        k = 0
        while k < i and promising:
            if col[i] == col[k] or abs(col[i] - col[k]) == abs(i - k):
                promising = False
            k += 1
        if promising:
            if i == n-1:
                answer += 1
                return
            for j in range(n):
                col[i+1] = j
                queens(i+1, n)

    queens(-1, n)
    return answer

print(solution(n))
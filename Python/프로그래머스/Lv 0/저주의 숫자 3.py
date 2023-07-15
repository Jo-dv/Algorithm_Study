n = 15

def solution(n):
    answer, i = 1, 1

    while True:
        if answer % 3 == 0 or '3' in str(answer):
            answer += 1
            continue
        i += 1
        if i > n:
            break
        answer += 1

    return answer

print(solution(n))
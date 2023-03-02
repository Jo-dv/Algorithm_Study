n = 45

def solution(n):
    answer = 0
    temp = []

    while n > 0:
        temp.insert(0, n % 3)
        n //= 3

    for i, digit in enumerate(temp):
        answer += 3 ** i * digit

    return answer



print(solution(n))



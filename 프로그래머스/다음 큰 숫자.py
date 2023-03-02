n = 15

def solution(n):
    result = n
    while True:
        result += 1
        if bin(n)[2:].count('1') == bin(result)[2:].count('1'):
            break

    return result

print(solution(n))
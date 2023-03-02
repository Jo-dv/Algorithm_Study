n = 3

def solution(n):
    temp = [0, 1]
    for i in range(2, n + 1):
        temp.append(temp[i - 1] + temp[i - 2])
    return temp[-1] % 1234567

print(solution(n))
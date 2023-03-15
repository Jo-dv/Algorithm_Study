n = 420

def solution(n):
    temp = [True for _ in range(n + 1)]

    for i in range(2, int(n ** 0.5) + 1):  # 소수 탐색
        if temp[i]:
            for j in range(i ** 2, n + 1, i):
                temp[j] = False
    num = [i+2 for i, j in enumerate(temp[2:]) if j]  # 소수의 여부를 소수로 변환

    return [i for i in num if n % i == 0]  # 주어진 수가 n이하의 소수로 나눠진다면 저장

print(solution(n))
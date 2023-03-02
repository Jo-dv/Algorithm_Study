n = 20

def solution(n):
    a = [(i, n // i) for i in range(1, int(n**0.5)+1) if n % i == 0]  # 속도 개선
    return len(a) * 2 + (0 if a[-1][0] != a[-1][1] else -1)  # 마지막 값이 대칭이면 해당 대칭 값 제외

print(solution(n))
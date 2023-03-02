a, b, n = 3, 1, 20

def solution(a, b, n):
    bundle, rest, answer = 0, 0, 0
    while n >= a:
        bundle, rest = divmod(n, a)  # 묶음과 묶고난 나머지
        n = bundle * b + rest  # 총 수량 = 묶음 * 교환가능한 수 + 나머지
        answer += bundle * b  # 교환한 콜라의 수 = 묶음 * 교환가능한 수의 총 합
    return answer

print(solution(a, b, n))
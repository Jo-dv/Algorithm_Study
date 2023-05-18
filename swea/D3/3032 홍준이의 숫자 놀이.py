def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0  # 초기 x, y는 이전 값이 없으므로 1과 0으로 초기화
    gcd, x1, y1 = extended_gcd(b, a % b)  # 이후 x와 y는 각각 이들을 역으로 사용, x는 y, y는 x
    x = y1
    y = x1 - y1 * (a // b)
    return gcd, x, y


for t in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    gcd, x, y = extended_gcd(A, B)  # 선형 방정식 ax + by = c, c는 최대공약수의 배수임을 따른다.(c % gcd(a, b) == 0일 때)
    if gcd != 1:
        print(f"#{t} -1")
    else:
        print(f"#{t} {x} {y}")

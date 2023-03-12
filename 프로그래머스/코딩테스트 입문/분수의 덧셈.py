numer1, denom1, numer2, denom2 = 1, 2, 3, 4

def solution(numer1, denom1, numer2, denom2):
    def gcd(n, m):
        if m == 0:
            return n
        return gcd(m, n % m)
    n, m = numer1 * denom2 + numer2 * denom1, denom1*denom2  # 분수계산식
    b = gcd(n, m)  # 최대공약수를 구하여
    return [n // b, m // b]  # 기약분수 계산
    # 덧붙여, (n * m)//b = 최소공배수

print(solution(numer1, denom1, numer2, denom2))
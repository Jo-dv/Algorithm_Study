n = 4

def solution(n):
    def gcd(n, m):
        if m == 0:
            return n
        return gcd(m, n % m)
    b = gcd(n, 6)  # 최대공약수
    answer = b * (n // b) * (6 // b)  # 최대공약수를 이용한 최대공배수
    return answer // 6  # 최대 공배수를 6으로 나누면 피자의 수

print(solution(n))
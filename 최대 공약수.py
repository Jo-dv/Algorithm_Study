n, m = 20, 12

def solution(n, m):
    def gcd(n, m):
        if m == 0:
            return n
        return gcd(m, n % m)
    b = gcd(n, m)
    return [b, n * m // b]

print(solution(n, m))
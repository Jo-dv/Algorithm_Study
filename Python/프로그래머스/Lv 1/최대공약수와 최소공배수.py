from functools import reduce

n = 60
m = 3

def solution(n, m):
    i = 2
    gcd = [1]
    while i < int((n * m)**0.5) + 1:
        if n % i == 0 and m % i == 0:
            gcd.append(i)
            n //= i
            m //= i
            continue
        i += 1
    lcm = gcd + [n] + [m]
    return [reduce(lambda x, y: x * y, gcd), reduce(lambda x, y: x * y, lcm)]

print(solution(n, m))

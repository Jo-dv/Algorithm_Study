balls, share = 3, 2

def solution(balls, share):
    n, m, nm = 1, 1, 1
    for i in [i for i in range(balls, 0, -1)]:
        n *= i
    for i in [i for i in range(share, 0, -1)]:
        m *= i
    for i in [i for i in range(balls-share, 0, -1)]:
        nm *= i
    return n // (nm * m)

print(solution(balls, share))
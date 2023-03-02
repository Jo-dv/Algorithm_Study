from functools import reduce
arr = [2, 6, 8, 14]

def solution(arr):
    arr.sort(reverse=True)

    def gcd(n, m):
        if m == 0:
            return n
        return gcd(m, n % m)

    gcds = [gcd(arr[0], arr[1])]

    for i in range(2, len(arr)):
        gcds.append(gcd(arr[i], gcds[-1]))

    print(gcds)
    return reduce(lambda x, y: x * y, [i // gcds[-1] for i in arr]) * gcds[-1]

print(solution(arr))
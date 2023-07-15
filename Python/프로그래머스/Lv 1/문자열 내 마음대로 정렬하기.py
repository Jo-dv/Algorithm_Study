strings = ["abce", "abcd", "cdx"]
n = 2


def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x))
    return strings


print(solution(strings, n))
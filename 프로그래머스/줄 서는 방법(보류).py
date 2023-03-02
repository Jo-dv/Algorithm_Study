from itertools import islice, permutations

n = 4
k = 5


def solution(n, k):
    print(list(permutations(range(1, n+1))))
    return list(map(list, (islice(permutations(range(1, n+1)), k-1, k))))[0]


print(solution(n, k))
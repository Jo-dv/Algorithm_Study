land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]


def solution(land):
    global answer, N, stamp, check
    answer = 0
    N = len(land)
    stamp = [0] * N
    check = [[False for _ in range(4)] for _ in range(N+1)]

    def search(k, land):
        global answer
        if k == N+1:
            if answer < sum(stamp):
                answer = sum(stamp)
            return
        for i in range(4):
            if not check[k-1][i]:
                check[k][i] = True
                stamp[k-1] = land[k-1][i]
                search(k + 1, land)
                check[k][i] = False

    search(1, land)
    return answer

print(solution(land))

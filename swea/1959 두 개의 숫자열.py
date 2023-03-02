import math
T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    size = min(N, M)  # 움직일 list의 길이
    stride = abs(N - M) + 1  # 계산 횟수
    res = -math.inf

    move, fixed = min(Ai, Bj, key=lambda x: len(x)), max(Ai, Bj, key=lambda x: len(x))
    # 길이가 짧은 list를 움직일 list, 긴 list를 고정된 list, key를 통해 조건에 맞는 list를 반환

    for j in range(stride):
        s = sum([i * j for i, j in zip(move, fixed[0+j:j+size])])  # 움직이는 list와 마주보는 구간을 계산
        res = max(res, s)
    print(f'#{i} {res}')
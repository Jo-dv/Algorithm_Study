T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    midnight = A + B
    if midnight >= 24:  # 자정이거나 자정을 넘기면
        res = midnight - 24  # 자정만큼 빼줌
    else:
        res = midnight

    print(f'#{i} {midnight}')
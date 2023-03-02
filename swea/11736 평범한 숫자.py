for t in range(1, int(input())+1):
    N = int(input())
    permu = list(map(int, input().split()))
    count = 0

    for i in range(1, N-1):  # i와 양 측면을 비교하기 위해 두 번째 값부터 마지막 이전 값까지
        minimum, maximum = min(permu[i-1:i+2]), max(permu[i-1:i+2])  # list 전체의 최소 및 최대가 아니라 i가 결정된 시점에서
        if permu[i] != minimum and permu[i] != maximum:  # 중간값이 최소도 최대도 아닐경우
            count += 1

    print(f'#{t} {count}')
for i in range(1, 11):
    N = int(input())
    apart = list(map(int, input().split()))
    count = 0

    for j in range(2, len(apart)-2):  # 측면의 땅을 제외하고
        check = min([apart[j]-apart[j-2], apart[j]-apart[j-1], apart[j]-apart[j+1], apart[j]-apart[j+2]])
        # 현재 아파트를 기준으로 양쪽 두 아파트와의 차이를 구함, 이때 차이의 최소가 양수일 경우 해당 아파트에서 조망권이 확보된 세대
        # 음수일 경우 조망권이 확보되지 않은 아파트
        if check > 0:  # 조망권이 확보된 세대들의 수를 누적
            count += check

    print(f'#{i} {count}')
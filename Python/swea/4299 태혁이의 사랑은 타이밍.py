for t in range(1, int(input())+1):
    D, H, M = map(int, input().split())

    if (D == 11 and H < 11) or (D == 11 and H == 11 and M < 11):  # 날은 같고(11) 시간이 빠르거나 시간은 같은데 분이 빠르다면
        res = -1  # 약속 시간보다 빨리 차였으므로
    else:  # 그 외는
        D, H, M = D - 11, H - 11, M - 11  # 입력 받은 조건에서 기준 만큼 빼고
        res = 60 * 24 * D + 60 * H + M  # 분으로 환산하여 합
    print(f'#{t} {res}')
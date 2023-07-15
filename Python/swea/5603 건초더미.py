for t in range(1, int(input())+1):
    N = int(input())
    hay = [int(input()) for _ in range(N)]
    height = sum(hay) // len(hay)  # 모든 건초더미의 높이가 같으므로 건초더미의 높이의 평균이 원래 모든 건초더미의 높이
    res = 0

    for i in hay:  # 건초더미 하나에 한 번 이동
        if height - i > 0:  # 값이 음수라면 평균보다 높기 때문에 평균보다 낮은 더미로 이동할 더미의 수를 뜻함
            res += (height - i)
            # 예를 들어 총 7번을 옮긴다면 +7과 -7 도합 0이 되므로 음수만 확인하거나 양수만 확인하면 됨, 편의상 양수를 더함

    print(f'#{t} {res}')

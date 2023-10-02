for t in range(1, int(input())+1):
    D, L, N = map(int, input().split())
    damage = 0

    for n in range(N):  # 데미지 누적
        damage += D*(1+n*(L*0.01))  # 식 그대로 표현: D(1+nㆍL%) | % = 1 / 100

    print(f'#{t} {int(damage)}')
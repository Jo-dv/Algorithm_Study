T = int(input())

for i in range(1, T+1):
    p, q = map(float, input().split())
    # s1 = 한 번 뒤집어서 성공하므로 첫 상태는 무조건 뒤집은 상태: 1-p, 그 후 올바르게 뒤집어서 성공하므로 q
    # s2 = 두 번 뒤집어서 성공하므로 첫 상태는 맞으나 q에 따라 실패: p*(1-q), 첫 모양이 맞으므로 뒤집으면 무조건 실패, 그 다음 다시
    # 뒤집어서 q, 결과적으로 p*(1-q)*q
    # s1과 s2의 첫 상태를 결정할 때만 확률에 의해 결정되고 이후 뒤집어서 상태를 바꾸는 것은 필연적이므로 확률에 영향 없음
    s1, s2 = (1-p), p * (1-q)  # s1 < s2 양 변에 q는 소거

    if s1 < s2:
        print(f'#{i} YES')
    else:
        print(f'#{i} NO')
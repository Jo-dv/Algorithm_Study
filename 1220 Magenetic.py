for i in range(1, 11):
    size = int(input())
    field = [list(map(int, input().split())) for _ in range(size)]

    t = [list(i) for i in zip(*field)]  # 열에 대해서만 보면 되므로 계산이 편하도록 전치행렬로 변환
    modified = [[j for j in i if j != 0] for i in t]  # 전치행렬에서 0 제거, 실질적으로 자성체들의 움직임을 표현
    res = [i[j:j+2] for i in modified for j in range(len(i)) if i[j:j+2] == [1, 2]]
    # 자성체들의 움직임이 끝난 상태에서 한 줄씩 가져와 교착 상태가(1, 2) 존재하는지 탐색, 존재하면 list에 추가

    print(f'#{i} {len(res)}')  # 교착 자성체의 개수 = list의 길이
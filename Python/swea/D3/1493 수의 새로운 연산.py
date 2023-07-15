def obtain(target, op):
    coord = [1, 1]  # 시작 좌표
    y, res = 1, 1  # 초기 y축, 초기값

    while True:
        cond = res == target if op == 0 else coord == target  # op에 따라 숫자를 좌표로 바꿀 건지 좌표를 숫자로 바꿀 건지 결정
        if cond:  # 타깃을 찾았다면
            break  # 반복 종료
        if coord[1] == 1:  # 좌표의 y가 1이라면
            y += 1  # y축 갱신
            coord[0], coord[1] = 1, y  # 다음 탐색을 위해 x = 1 y = y + 1로 초기화
        else:  # 좌표의 y가 1이 아니라면
            coord[0] += 1  # x값 증가
            coord[1] -= 1  # y값 감소
        res += 1  # 실행 횟수 갱신, 실행 횟수는 곧 찾고자 하는 숫자와 동일함

    return coord if op == 0 else res  # op에 따라 좌표를 반환하거나 숫자를 반환
# 그림으로 주어진 화살표를 따라 숫자를 나열해 보면 패턴을 알 수 있음
# 1(1 1)
# 2(1 2) 3(2 1)
# 4(1 3) 5(2 2) 6(3 1)
# ...
# x의 시작은 항상 1이면 y가 증가할수록 숫자의 개수도 따라 증가, 또한 숫자는 해당 y의 값이 1이 될 때까지 x는 증가, y는 감소하는 패턴을 보임

for t in range(1, int(input()) + 1):
    p, q = map(int, input().split())
    p_ = obtain(p, 0)  # 좌표 값 획득
    q_ = obtain(q, 0)
    p_q = [p_[0] + q_[0], p_[1] + q_[1]]  # 좌표 값 연산
    print(f'#{t} {obtain(p_q, 1)}')  # 연산한 좌표 값을 바탕으로 숫자 획득

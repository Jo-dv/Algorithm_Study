T = int(input())

for i in range(1, T + 1):
    N = int(input())
    res, speed = 0, 0

    for j in range(N):
        try:  # 기본 입력
            c, v = map(int, input().split())
        except ValueError:  # command가 0일 경우 단일 값만 들어오므로 기본 입력으로 받으면 오류가 발생하므로 예외 처리 수행
            c, v = 0, speed  # command가 0이면 기존 속도 유지이므로 v는 전의 speed를 받는다.

        if c == 1:  # 증가
            speed += v
        if c == 2:  # 감소
            speed = max(0, speed - v)  # 현재 속도보다 감속할 속도가 더 크면 음수가 나므로 최소 limit을 0으로 걸어둠
        res += speed  # 문제에서 m/s로 표현하므로 speed를 누적해 이동 거리 계산

    print(f'#{i} {res}')
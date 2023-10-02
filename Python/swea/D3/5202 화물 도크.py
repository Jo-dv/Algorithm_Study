for i in range(1, int(input())+1):
    n = int(input())
    time = [tuple(map(int, input().split())) for _ in range(n)]  # 작업 시간을 입력으로 받아 저장
    time.sort(key=lambda x: x[1])  # 저장된 작업 시간을 종료 시간을 기준으로 정렬
    answer = 0
    last = 0

    for j in time:  # 작업 시간을 불러와
        if last <= j[0]:  # 마지막으로 작업한 시간이 현재 작업할 시간보다 이전이라면
            answer += 1  # 작업 수행
            last = j[1]  # 마지막으로 작업한 시간을 현재 작업 시간의 종료 시간으로 갱신

    print(f'#{i} {answer}')
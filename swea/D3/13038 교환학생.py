from math import inf

for t in range(1, int(input())+1):
    n = int(input())
    schedule = list(map(int, input().split()))
    days = [i for i in range(7) if schedule[i]]  # 어느 날짜가 가장 최단 기간만에 알 수 없지만 무조건 수업하는 날 시작해야 이득
    answer = inf

    for i in days:  # 수업이 있는 날들만 확인해서
        day = 1  # 해당 수업 기준 소요 기간
        sub = n - 1  # 이미 그날 수업을 들었다고 가정하고 들어야 할 수업 -1
        while sub != 0:  # 수업을 다 들을 때까지
            i += 1  # 시간표를 통해 수업을 확인할 요일 인덱스 증가
            day += 1  # 머무는 날 증가
            if schedule[i % 7]:  # 수업이 있는 날이라면
                sub -= 1  # 들어야할 수업 수 감소
        answer = min(day, answer)  # 해당 날을 기준으로 최소 소요기간으로 갱신, 이후 모든 수업 날을 기준으로 최소 값 갱신됨

    print(f'#{t} {answer}')

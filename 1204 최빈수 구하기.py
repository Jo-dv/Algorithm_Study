T = int(input())

for i in range(1, T + 1):
    n = int(input())
    scores = [i for i in map(int, input().split())]  # 문제 입력
    frequency = {i: scores.count(i) for i in range(0, 101)}  # dictionary 형태로 빈도 계산
    res = sorted([i for i in frequency.items()], key=lambda x: (x[1], x[0]))
    # dictionary의 item을 list의 element로 하여 빈도와 값 순서로 정렬, 동일한 빈도일 경우 값 순서로 정렬

    print(f'#{i} {res[-1][0]}')
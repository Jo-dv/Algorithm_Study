T = int(input())

for i in range(1, T+1):
    N = int(input())
    num = {i: 0 for i in range(10)}  # 0~9를 키로, 본 횟수를 0으로 하여 dictionary 초기화
    x = 0  # 센 횟수 초기화

    while sum(num.values()) != 10:  # 모든 숫자를 다 볼 때까지, 0~9까지 다 보게 되면 
        x += 1  # 센 횟수 증가
        for j in str(x*N):  # 문제에서 제시한 조건, xN번의 양 세기
            if num[int(j)] == 0:  # 지금까지 안 본 숫자라면
                num[int(j)] = 1
    print(f'#{i} {x*N}')

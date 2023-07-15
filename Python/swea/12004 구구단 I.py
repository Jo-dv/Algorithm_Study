T = int(input())

for i in range(1, T + 1):
    N = int(input())

    for j in range(1, 10):
        if 1 <= N // j <= 9 and N % j == 0:  # 1 ~ 9 사이의 숫자로 나누어 떨어진다면
            print(f'#{i} Yes')
            break
    else:
        print(f'#{i} No')  # 해당 코드가 실행된다는 것은 주어진 범위의 숫자로 표현할 수 없음, 즉 a와 b의 곱으로 표현 불가

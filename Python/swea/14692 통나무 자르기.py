for t in range(1, int(input())+1):
    log = int(input())

    if log % 2 == 0:  # 모든 나무를 N:1의 비율로 자르면 된다. N:1, N-1:1, N-2:1, ... , 2:1, 1:1
        print(f'#{t} Alice')  # 이 규칙을 따르면 짝수일 때 Alice, 홀수일 때 Bob이 승리한다.
    else:
        print(f'#{t} Bob')
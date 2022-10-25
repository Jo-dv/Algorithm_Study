T = int(input())

for i in range(1, T+1):
    N = input()

    if int(N[-1]) % 2 == 0:  # 문자열로 입력 받아 끝에 한 자리만 홀수인지 짝수인지 검사, 좀 새롭개 풀어포고 싶었음
        print(f'#{i} Even')
    else:
        print(f'#{i} Odd')
for t in range(1, int(input())+1):
    s = input()
    start, end = 0, len(s) - 1

    for i in range(len(s)//2):
        if s[start] == '*' or s[end] == '*':
            # *는 길이 0이상의 문자열로 대치 가능, 즉 중간 기준으로 대칭이 맞지 않더라도 지금까지 대칭이었다면 팰린드롬 생성 가능
            # *가 만능은 아님 예를 들어, z*a와 같이 처음부터 틀렸기에 아무리 문자열을 추가해도 생성할 수 없음
            # 지금까지 대칭이 맞고 중간에 *가 나오면 * 이후부터 탐색하지 않은 범위에 대해 대칭되는 문자열 생성 가능
            print(f'#{t} Exist')
            break
        elif s[start] != s[end]:  # *가 없는 경우 대칭 검사
            print(f'#{t} Not exist')
            break
        start += 1  # 탐색 위치 조정
        end -= 1
    else:  # 길이가 홀수일 때, 가운데 *가 있어도 탐색하지 않기 때문에 조건문에 걸리지 않음, 그렇기에 정상적인 종료는 팰린드롬으로 간주
        print(f'#{t} Exist')
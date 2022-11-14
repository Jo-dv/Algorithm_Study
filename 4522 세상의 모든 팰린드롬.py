for t in range(1, int(input()) + 1):
    case = input()
    ans = 'Not exist'

    for i, j in zip(case, case[::-1]):  # 양 끝단을 비교
        if i != j and i != '?' and j != '?':  # 둘이 같지 않음과 동시에 모두 물음표가 아니라면
            break  # False, 양 끝단이 다르더라도 a?, ?a 의 형태는 괜찮음, ? 자리에 a만 들어오면 되기때문
    else:
        ans = 'Exist'  # 정상적으로 종료되었다면

    print(f'#{t} {ans}')

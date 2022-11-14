for t in range(1, int(input())+1):
    case = sorted(list(input()))  # 문자열 정렬
    if case[0] == case[1] and case[1] != case[2] and case[2] == case[3]:  # 가운데를 기준으로 양쪽이 서로 다르고 0~1, 2~3이 서로 각각 같다면
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')


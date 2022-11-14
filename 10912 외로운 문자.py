for t in range(1, int(input())+1):
    case = list(input())

    for i in range(len(case)):  # 왼쪽부터 순서대로 탐색
        if case[i] == '':  # 공백일 경우 넘어감
            continue
        for j in range(i+1, len(case)):  # i를 기준으로 한 칸 옆부터 완전 탐색
            if case[i] == case[j]:  # i와 j의 값이 같다면
                case[i] = case[j] = ''  # 공백으로 변경

    res = ''.join(sorted(case))  # list의 문자들을 알파벳순으로 정렬하여 하나의 문자열로 결합

    if res == '':  # 공백 문자열이라면
        print(f'#{t} Good')
    else:
        print(f'#{t}', res)
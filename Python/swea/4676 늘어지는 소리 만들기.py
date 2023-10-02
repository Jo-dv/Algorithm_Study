for t in range(1, int(input())+1):
    case = list(input())
    case.insert(0, '')  # 삽입 index를 맞추기 위해 앞단에 공백 삽입
    H = int(input())
    pos = list(map(int, input().split()))  # 위치 index를 입력
    check = ''  # 하이픈을 추가한 문자열을 만들기 위한 임시 변수
    hyphen = ['-']*H  # H를 사용하기 위해 하이픈 리스트 생성, 파이썬에서는 선언하지 않아도 됨

    for i in pos:
        check = case[i] + hyphen.pop()  # 하이픈을 꺼네 원래 문자열의 지정된 위치에 삽입
        case[i] = check  # 만들어진 문자열 재삽입

    print(f'#{t}', ''.join(case))
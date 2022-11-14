def I(data: list, x, y, s):  # 주어진 x는 값이 아닌 위치를 의미, 단 순서를 0부터 시작한 것이 아니라 1부터 시작
    for i in range(y - 1, -1, -1):  # 입력받은 list의 값을 순서대로 삽입할 경우, 결과적으로 역순이 되므로 애초에 역순으로 삽입
        data.insert(x, s[i])  # insert는 주어진 index에 값이 있다면 그 값을 뒤로 밀어내고 주어진 값을 그 자리에 삽입
        # 문제의 제시 조건 특성상 x의 뒤에 값을 삽입하는 것인데 x자체가 +1 되어있으므로 0부터 시작하는 list에 x를 그대로 사용해야 함


def D(data: list, x, y):
    for _ in range(y):  # y번 만큼 x의 위치에 존재하는 값는 제거
        del data[x]

for i in range(1, 11):
    N = int(input())
    original = input().split()  # 원본 암호
    com_num = int(input())
    com = input().split()  # 명령어

    temp = None
    split_com = []  # 명령어 분할을 위한 list
    for j in com:
        if j.isalpha():
            if temp:  # temp가 빈 list가 아니라면 한 명령어 구성이 있다는 뜻이므로
                split_com.append(temp)  # 전 시점의 분할된 명령어 추가
            c = j  # 명령어 내용을 저장하여
            temp = [c]  # 리스트로 생성
            continue
        temp.append(j)  # 다음 알파벳이 나오기 전까지 명령어의 처리 내용이므로 명령어 내용이 저장되어있는 list에 저장
    split_com.append(temp)  # 반복이 끝날 경우 마지막 명령어 추가없이 끝나므로 마지막 명령을 추가

    for j in split_com:  # 분할된 명령어에서
        if j[0] == 'I':
            I(original, int(j[1]), int(j[2]), j[3:])
        else:
            D(original, int(j[1]), int(j[2]))
    # 파이썬의 list들은 기본적으로 주소 참조 방식을 사용하므로 별도의 return을 수행하지 않아도 된다.
    print(f'#{i}', *original[:10])

for t in range(1, int(input())+1):
    n = int(input())
    s = ''
    end_count = 0  # 구두점의 수, 즉 입력 받은 문장의 수가 n과 같다면 종료
    while end_count != n:  # 제공되는 파일과 예제와 다름, 예제를 기준으로 문제를 풀지 않으면 런타임 에러 발생
        temp = input().replace('!', '.').replace('?', '.')  # 문장의 구두점을 온점으로 통일
        s += temp + ' '  # 다음 문장을 받기 위해 마지막에 공백 추가
        end_count += temp.count('.')  # 입력 받은 문장에서 구두점 갯수 카운팅
    answer = [0] * n
    check = False  # 구두점 확인용 플래그
    idx = 0

    for i in s.rstrip().split():  # 전처리 과정에서 문장 끝에 추가된 공백을 제거하고 공백을 기준으로 단어를 나눔
        if i[-1] == '.':  # 단어에 구두점이 포함되어 있으면
            i = i[:-1]  # 제외
            check = True  # 플래그 활성화
        if i[0].isupper() and (len(i) == 1 or (i[1:].isalpha() and i[1:].islower())):
            # 첫 글자가 대문자이면서 문정의 길이가 1이거나 그렇지 않을 경우 첫 글자 이후 전부 알파벳인 동시에 소문자일 경우
            answer[idx] += 1  # 해당 문장의 결과 갱신
        if check:  # 플래그가 화성화 돼있다면
            idx += 1  # 다은 문장으로 넘어가기 위해 정답을 갱신할 인덱스 갱신
            check = False  # 다음 문장 검사를 위해 플래그 비활성화

    print(f'#{t}', *answer)
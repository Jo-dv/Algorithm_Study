for t in range(1, int(input())+1):
    words = [input() for _ in range(5)]

    ml = len(max(words, key=len))  # 단어 중, 최대 길이 탐색
    words = [i if len(i) == ml else i+" "*(ml-len(i)) for i in words]  # 최대 길이에 맞춰 부족한 단어는 공백으로 채움
    t_words = [''.join(i).replace(' ', '') for i in zip(*words)]  # 단어들을 세로 형태로 가져오되, 공백은 제거해서 가져옴
    res = ''.join(t_words)  # list의 모든 문자열을 하나로 합침

    print(f'#{t}', res)
T = int(input())

vowel = ['a', 'e', 'i', 'o', 'u']

for i in range(1, T+1):
    word = list(input())

    for j in range(len(word)):
        if word[j] in vowel:  # j번째 문자가 모음이라면
            word[j] = ""  # 공백으로 치환

    print(f'#{i}', ''.join(word))  # 문자열 리스트를 문자열로 변환
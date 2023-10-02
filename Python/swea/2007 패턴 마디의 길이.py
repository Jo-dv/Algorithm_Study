T = int(input())

for i in range(1, T+1):
    case = input()
    slicing = 1
    while case[0:slicing] != case[slicing:2*slicing]:
        # 왼쪽부터 한 글자씩 확인해서 하나의 단어(마디)가 되면, 그 단어 이후부터 단어의 길이배까지의 문자열은 해당 단어(패턴)가 된다.
        slicing += 1  # 한 단어가 될 때까지 슬라이싱 범위를 1씩 증가
    print(f'#{i} {slicing}')
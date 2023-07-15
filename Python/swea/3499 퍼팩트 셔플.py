for t in range(1, int(input())+1):
    N = int(input())
    deck = input().split()
    shuffled, rest = [], []

    if N % 2 != 0:  # 덱의 길이가 홀수라면
        left, right, rest = deck[:N//2], deck[N//2+1:], deck[N//2]  # 가운데를 기준으로 좌우로 나누고 가운데를 나머지로 둠
    else:  # 아니라면 그냥 반으로 나눔
        left, right = deck[:N // 2], deck[N // 2:]

    for i, j in zip(left, right):  # 좌, 우를 번갈아서 저장
        shuffled.append(i)
        shuffled.append(j)
    if rest:  # 나머지 카드가 있을 경우
        shuffled.append(rest)

    print(f'#{t}', ' '.join(shuffled))

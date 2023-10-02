t = int(input())

for i in range(t):
    n, l, f = map(int, input().split())
    words = list(input().split())
    answer = 0
    hash = {}

    for i in words:  # 각 단어를 가져와서
        if i[-f:] in hash:  # 접미사가 hash에 있다면
            hash[i[-f:]] += 1  # 갱신
        else:
            hash[i[-f:]] = 1  # 없다면 추가
    print(sum(i // 2 for i in hash.values() if i > 1))  # 값이 2 이상부터 최소 하나의 짝을 만들 수 있고
    # 해당 문제는 짝을 만들 수 있는 경우의 수가 아닌 그 게임에서 만들 수 있는 최대, 즉 앞에서부터 순서대로 짝을 만든 다는 것
    # 가령 7이 나왔다면 7C2가 아니라 (1, 2), (3, 4), (5, 6), 7 = 만들 수 있는 짝은 3개이고 이건 동일한 게임에 대해서 고정된 값
    # 처음 sum(i for i in hash.values() if i > 1) // 2로 계산을 해서 실수
    # 이 코드는 각 경우가 아니라 모든 경우를 합쳐서 짝을 만들기에 오류임, 예를 들어 {7, 7, 7} 이라면 총 9개의 짝을 만들어야 하지만
    # 총합에서 짝을 나누면 10이 되므로 맞지 않음
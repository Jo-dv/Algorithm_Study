'''
for i in range(1, int(input()) + 1):  # 정렬을 함으로써 뽑는 순서를 무시해버리는 코드
    cards = list(map(int, input().split()))
    p1, p2 = [], []
    for j in range(len(cards)):
        p1.append(cards[j]) if j % 2 == 0 else p2.append(cards[j])
    p1.sort()
    p2.sort()

    for j in range(4):  # 순서를 무시하고 단지 유효성만 평가하므로, 원래 순서대로라면 p2가 승자일지라도 p1이 승리할 수도 있게 됨
        p1_card = p1[j:j + 3]  # 즉 후반에 p1이 완성되고, 초반에 p2가 완성되어서 p2가 이기게 되더라도 정렬을 했기 때문에 p1이 승리
        p2_card = p2[j:j + 3]
        if p1_card == [p1_card[0]] * 3 or p1_card == list(range(p1_card[0], p1_card[0] + 3)):
            print(f'#{i} {1}')
            break
        elif p2_card == [p2_card[0]] * 3 or p2_card == list(range(p2_card[0], p2_card[0] + 3)):
            print(f'#{i} {2}')
            break
    else:
        print(f'#{i} {0}')
'''
def check(cards):
    for i in range(8):  # 인덱스를 3개의 세트로 하여
        if cards[i] >= 1 and cards[i+1] >= 1 and cards[i+2] >= 1:  # 연속되는 3개의 카드가 전부 1이상이라면
            return True
    for i in range(10):  # 특정 인덱스의 카드가 3장 이상 뽑혀있다면
        if cards[i] >= 3:
            return True
    return False

for i in range(1, int(input()) + 1):
    cards = list(map(int, input().split()))
    p1, p2 = [0] * 10, [0] * 10  # 카드를 뽑은 상태를 저장하는 리스트
    answer = 0

    for j in range(len(cards)):
        if j % 2 == 0:  # p1이 뽑은 카드를 인덱스로 하여 값 갱신
            p1[cards[j]] += 1
            if check(p1):
                answer = 1
                break
        else:  # p2가 뽑은 카드를 인덱스로 하여 값 갱신
            p2[cards[j]] += 1
            if check(p2):
                answer = 2
                break

    print(f'#{i} {answer}')
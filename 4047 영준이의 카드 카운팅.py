from collections import Counter

for t in range(1, int(input())+1):
    deck = input()
    deck = [deck[i:i+3] for i in range(0, len(deck), 3)]  # 카드의 정보는 TXY 형태이므로 3글자씩 분리
    check = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    # Counter를 사용해서 카드의 개수를 counting
    if list(Counter(deck).values()) != [1]*len(deck):  # 만약 중복 되는 카드가 있다면 결과는 [1, n, 1, ... ,1] | n > 1의 형태
        print(f'#{t} ERROR')  # [1]*len(deck), len(deck)는 카드의 수를 의미
    else:  # 중복된 카드가 없다면
        for i in deck:
            check[i[0]] -= 1  # 각 카드의 T 정보를 key로 하여 해당 key의 value를 감소
        print(f'#{t}', *list(check.values()))  # 반복의 결과는 카드가 존재할 때 마다 1씩 감소했으므로 부족한 카드의 수가 순서대로 출력
        
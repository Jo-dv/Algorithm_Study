from collections import deque

cards1, cards2, goal = ["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]


def solution(cards1, cards2, goal):
    cards1, cards2 = deque(cards1), deque(cards2)

    for i in goal:  # 만들고자 하는 문장의 각 단어가 카드 뭉치의 가장 앞 장일 경우
        if cards1 and i == cards1[0]:  # 앞에 선행 조건으로 카트의 상태를 걸지 않으면 인덱스 오류 발생
            cards1.popleft()
        elif cards2 and i == cards2[0]:
            cards2.popleft()
        else:  # 만약 만들고자 하는 문장의 단어가 각 카드 뭉치의 첫 장으로 없을 경우, 이는 만들 수 없는 상태이므로
            return 'No'

    return 'Yes'  # 모든 카드를 다 뽑았기에


print(solution(cards1, cards2, goal))

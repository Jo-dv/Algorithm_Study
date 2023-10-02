from collections import deque

k, m, score = 4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

def solution(k, m, score):
    boxes, box, maximum = [], [], len(score) // m  # 최대로 생성할 수 있는 상자의 수
    score = deque(sorted(score, reverse=True))  # 최상품부터 박스 생성

    while len(boxes) != maximum:  # 상자를 최대로 만들어 낼 때까지
        box.append(score.popleft())  # 사과 상자에서 사과를 뽑아 박스에 저장
        if len(box) == m:  # 한 박스의 적재용량에 도달하였을 경우
            boxes.append(box)  # 해당 박스 저장
            box = []

    answer = sum([min(i)*m for i in boxes])  # 각 박스 기준 최하품의 점수와 적재용량을 곱하여 합함
    return answer

print(solution(k, m, score))
def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]  # 4 x 3 매트릭스
    pos = {k: (y, x) for y, lines in enumerate(keypad) for x, k in enumerate(lines)}  # 각 키에 대한 위치 저장
    l_hand, r_hand = '*', '#'  # 처음 시작 위치

    for target in numbers:  # 눌러야 할 번호가
        if target in list(zip(*keypad))[0]:  # 누를 수 있는 곳이 왼쪽에 위치해 있다면
            l_hand = target  # 왼손은 해당 번호로 이동
            answer += 'L'  # 그리고 왼손을 사용했으므로 답에 왼손 추가
        elif target in list(zip(*keypad))[2]:  # 누를 수 있는 곳이 오른쪽에 위치해 있다면
            r_hand = target  # 오른손을 해당 번호로 이동
            answer += 'R'  # 그리고 오른손을 사용했으므로 답에 오른손 추가
        else:  # 가운데에 위치해 있다면
            l_distance = sum([abs(i - j) for i, j in zip(pos[l_hand], pos[target])])  # 상하좌우만 움직일 수 있으므로 맨해튼 거리 계산
            r_distance = sum([abs(i - j) for i, j in zip(pos[r_hand], pos[target])])  # 대각선 이동에 대한 거리는 유클리드
            if l_distance > r_distance:  # 거리가 오른쪽이 더 가깝다면
                r_hand = target
                answer += 'R'
            elif l_distance == r_distance:  # 두 거리가 동일할 경우
                if hand == 'left':  # 자신의 주 손에 따라
                    l_hand = target
                else:
                    r_hand = target
                answer += hand[0].upper()  # hand의 값은 left 또는 right이므로 첫 글자를 가져와 대문자로 변환 후 추가
            else:  # 왼쪽이 더 가깝다면
                l_hand = target
                answer += 'L'
    return answer


targets = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

print(solution(targets, hand))
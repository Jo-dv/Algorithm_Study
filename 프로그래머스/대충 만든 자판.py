keymap, targets = ["ABACD", "BCEFD"], ["ABCD", "AABB"]

def solution(keymap, targets):
    pad, answer = {i: list(j) for i, j in enumerate(keymap)}, []  # 각 키에 문자열을 할당한 키패드 생성

    for i in targets:  # 타켓을 하나씩 불러와서
        cnt = 0
        for target in i:  # 타켓에서 한 문자씩 불러와서
            x = [pad[i].index(target) + 1 if target in pad[i] else -1 for i in range(len(keymap))]
            # 타켓이 키패드에 있다면 인덱스를 사용하여 가장 앞에서 일치하는 인덱스를 저장하고 없다면 -1저장
            # 예를 들어 i가 AAB이고 첫 타겟인 A에 대해 x가 [1, -1]이라면 키패드의 첫 번째 키를 한 번, 두 번째 키로 만들 수 없음을 의미
            if all(i == -1 for i in x):  # 키패드를 이용해서 타겟을 만들 수 없다면
                cnt = -1
                break  # 키패드 검사 중지
            cnt += min([i for i in x if i > -1])  # 중지가 되지 않았다면 -1을 제외한 최솟값을 누적
        answer.append(cnt)  # 최종적인 값 저장

    return answer

print(solution(keymap, targets))
s = 'abracadabra'


def solution(s):
    x, check, answer = '', 0, 0

    for i in s:
        if not x:  # 첫 글자 파싱
            x = i
            check += 1  # 첫 글자는 무조건 첫 글자와 동일하므로 +1
        else:
            check += 1 if i == x else -1  # 이후부터 x와 동일하면 +1 아니면 -1
            if check == 0:  # x와 같거나 다른 문자의 수가 같다면 0
                x, check = '', 0  # 다음 탐색을 위해 초기화
                answer += 1  # 분해 횟수 추가
    # 문제에서 제시하는 문자열 분리하는 것은 풀이에 아무 의미없음, 분리 시점에서 다음 문자를 첫 문자로 삼으면 되기 때문
    return answer + (1 if x else 0)  # 분리 시점에서 반복이 종료되었을 때 문자가 초기화되지 않았다면 해당 문자를 따로 분리한 것으로 간주


print(solution(s))

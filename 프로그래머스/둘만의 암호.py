from string import ascii_lowercase

s, skip, index = 'aukks', 'wbqd', 5

def solution(s, skip, index):
    answer = ''
    c = ''.join(i for i in ascii_lowercase if i not in skip)  # s와 skip은 중복되는 것이 없으므로 s만 순서대로 필터링
    key, val = {j: i for i, j in enumerate(c)}, {i: j for i, j in enumerate(c)}
    ub = len(c)  # 상한, 마지막 알파벳의 인덱스는 상한 = 필터링된 알파벳들의 길이와 과 같다.
    for i in s:  # 알파벳을 이용해 해당 알파벳의 인덱스 번호를 탐색
        answer += val[(key[i] + index) % ub]  # s는 순환 구조이므로 상한으로 나눴을 때 나머지로 인덱스가 순환됨

    return answer

print(solution(s, skip, index))
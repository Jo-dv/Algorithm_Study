from string import ascii_lowercase

s = 'hello'

def solution(s):
    check = {i: 0 for i in ascii_lowercase}
    for i in s:
        check[i] += 1
    return ''.join([i[0] for i in check.items() if i[1] == 1])  # 한 번만 나온 것에 대해서
    # 딕셔너리 자체가 알파벳 순서대로 되어 있기 때문에 별도로 정렬할 필요 없음

print(solution(s))
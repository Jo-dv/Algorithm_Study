str1, str2 = 'ab6CDE443fgh22iJKlmn1o', '6CD'


def solution(str1, str2):
    return 1 if str2 in str1 else 2


print(solution(str1, str2))

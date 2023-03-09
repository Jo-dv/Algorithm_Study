babbling = ["aya", "yee", "u", "maa", "wooye"]

def solution(babbling):
    for i, j in enumerate(babbling):
        temp = ''
        for k in j:  # 문자를 하나씩 붙이면서
            temp += k
            if temp in ["aya", "ye", "woo", "ma"]:  # 조합된 단어가 주어진 조건과 부합하면
                babbling[i] = babbling[i].replace(temp, '', 1)  # 해당 문자열에서 조합된 단어 제거
                temp = ''  # 조합된 단어 초기화

    return len([1 for i in babbling if i == ''])  # 주어진 조건으로만 조합된 단어는 공백으로 바뀌므로 공백 카운팅

print(solution(babbling))
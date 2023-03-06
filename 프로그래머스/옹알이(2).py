babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]

'''
def solution(babbling):
    check = ["aya", "ye", "woo", "ma"]
    for i, j in enumerate(babbling):
        temp = ''
        for k in j:
            temp += k
            if temp in check:
                babbling[i] = j.replace(temp, '')

    print(babbling)
    return sum([1 for i in babbling if i == ''])
'''


def solution(babbling):
    check = ["aya", "ye", "woo", "ma"]

    for i, j in enumerate(babbling):
        prev, temp = '', ''
        for k in j:  # 주어진 문제에서 한 글자씩 분리
            temp += k  # 다시 단어를 조합
            if temp in check and temp != prev:  # 조합된 단어가 기준에 부합하며 직전에 만들어진 단어가 아니라면
                babbling[i] = babbling[i].replace(temp, '', 1)  # 문제의 해당 단어를 공백으로 치환
                prev, temp = temp, ''  # prev는 연속된 단어를 탐지하기 위한 변수, temp와 prev가 같다면 해당 단어는 연속된 단어

    return len([1 for i in babbling if i == ''])  # 처리된 문제에서 공백만 카운팅


print(solution(babbling))

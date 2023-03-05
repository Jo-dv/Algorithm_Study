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
    node = {i: [] for i in ["aya", "ye", "woo", "ma"]}
    check = [[i] for i in babbling]

    for i in babbling:
        for j in node.keys():
            t = i.split(j)
            if t in check or not any(t):
                continue
            node[j].append(''.join(t))
    return node


print(solution(babbling))

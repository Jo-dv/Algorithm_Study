spell, dic = ['p', 'o', 's'], ["sod", "eocd", "qixm", "adio", "soo"]

def solution(spell, dic):
    temp = {i: [] for i in dic}
    for i in dic:  # 각 단어마다
        for j in spell:  # 스펠링의 수를 카운팅
            temp[i].append(i.count(j))
    return 1 if [1] * len(spell) in temp.values() else 2  # 카운팅 된 값이 스펠링에 대해 각각 1씩 있다면

print(solution(spell, dic))
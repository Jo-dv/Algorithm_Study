def solution(name, yearning, photo):
    dic = {n: s for n, s in zip(name, yearning)}  # 이름과 점수를 하나로 묶음, dict(zip(name,yearning))도 가능
    return [sum([dic[j] for j in i if j in dic.keys()]) for i in photo]  # 순서대로 딕셔너리에 이름이 있다면 점수 추가 후 합산

name, yearning, photo = ["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],
                                                                         ["may", "kein", "brin", "deny"],
                                                                         ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))
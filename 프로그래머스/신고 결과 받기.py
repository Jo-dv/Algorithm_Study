from collections import Counter

id_list = ["muzi",
           "frodo",
           "apeach",
           "neo"]

report = ["muzi frodo",
          "apeach frodo",
          "frodo neo",
          "muzi neo",
          "apeach muzi"]
k = 2

def solution(id_list, report, k):
    answer = []
    report = set(report)
    rel = {key: [i.split()[1] for i in report if key == i.split()[0]] for key in id_list}
    reported_user = [i.split()[1] for i in report]

    for value in rel.values():
        res = 0
        for key in value:
            if Counter(reported_user)[key] >= k:
                res += 1
        answer.append(res)

    return answer


print(solution(id_list, report, k))

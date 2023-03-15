n = 5
lost = [3, 4]
reserve = [4]

def solution(n, lost, reserve):
    temp = {}
    set1 = set(lost)
    set2 = set(reserve)
    lost = list(set1 - set2)
    reserve = list(set2 - set1)

    for i in reserve:
        if i == 1:
            temp[i] = [i + 1]
        else:
            temp[i] = [i - 1]
            temp[i].append(i + 1)

    for i in lost[:]:
        for values in temp.values():
            if i in lost and i in values:
                lost.remove(i)
                values.clear()
                break

    return n - len(lost)

print(solution(n, lost, reserve))
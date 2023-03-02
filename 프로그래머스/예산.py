d = [1,3,2,5,4]
budget = 9

def solution(d, budget):
    d.sort()
    res = answer = 0
    for i in d:
        res += i
        if res <= budget:
            answer += 1
    return answer

print(solution(d, budget))
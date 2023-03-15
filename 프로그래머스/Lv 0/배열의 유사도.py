s1, s2 = ["a", "b", "c"], ["com", "b", "d", "p", "c"]

def solution(s1, s2):
    return len(set(s1) & set(s2))

print(solution(s1, s2))
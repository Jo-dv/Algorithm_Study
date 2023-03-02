str1 = 'aa1+aa2'
str2 = 'AAAA12'

def solution(str1, str2):
    s1 = [(str1[i:i+2]).upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [(str2[i:i+2]).upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    intersection = [i for i in set(s1) & set(s2) for _ in range(min(s1.count(i), s2.count(i)))]
    union = [i for i in set(s1) | set(s2) for _ in range(max(s1.count(i), s2.count(i)))]

    if len(intersection) == len(union) == 0:
        return 65536
    else:
        return int(len(intersection) / len(union) * 65536)

print(solution(str1, str2))
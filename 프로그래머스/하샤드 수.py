x = int(input())

def solution(x):
    res = 0
    x = str(x)
    for i in x:
        res += int(i)
    return True if int(x) % res == 0 else False

print(solution(x))
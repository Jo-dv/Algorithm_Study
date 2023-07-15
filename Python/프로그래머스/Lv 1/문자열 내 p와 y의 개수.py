s = "pPoooyY"

def solution(s):
    s = s.upper()
    if s.count('P') == 0 and s.count('Y') == 0:
        return True
    elif s.count('P') == s.count('Y'):
        return True
    else:
        return False

print(solution(s))
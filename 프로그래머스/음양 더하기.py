absolutes = [4, 7, 12]
signs = [True, False, True]

def solution(absolutes, signs):
    answer = sum([val if sign else -val for val, sign in zip(absolutes, signs)])
    return answer

print(solution(absolutes, signs))
num, total = 5, 5

def solution(num, total):
    if total % num == 0:
        return list(range(total//num - num//2, total//num + num//2 + 1))
    else:
        return list(range(total//num - num//2 + 1, total//num + num//2 + 1))

    # 일반화 했을 때, total이 num으로 나눠 떨어지면 혹은 num이 홀수이면 total을 num으로 나눴을 때 몫을 기준으로 
    # 좌측과 우측이 num-1을 2만큼 나눴을 때의 몫만큼 퍼지게 됨, (num-1)//2 와 num//2는 동일함
    # total이 num으로 나눠 떨어지지 않거나 혹은 num이 짝수이면 total을 num으로 나눴을 때 몫을 기준으로 
    # 좌측은 num을 2로 나눴을 때의 몫 +1, 우측은 num을 2로 나눴을 때의 몫이 됨, total을 num으로 나눴을 때 몫은
    # 수열에서의 위치는 수열을 반으로 나눴을 때 좌측의 가장 끝에 위치함
    # ex) total: 27, num: 6, 2 3 [4] | 5 6 7
    #     total: 14, num: 4, 2 [3] | 4 5
    # 두 조건 다 우측에 +1을 해준 것은 range의 특성 때문
print(solution(num, total))

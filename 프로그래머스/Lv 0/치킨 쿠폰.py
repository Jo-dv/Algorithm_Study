chicken = 10

def solution(chicken):
    memo = [chicken]
    while memo[-1] > 10:  # 10 미만은 치킨을 시켜먹을 수 없음
        memo.append(sum(divmod(memo[-1], 10)))  # 다음 쿠폰의 수는 현재 쿠폰의 수에서 10으로 나눈 몫과 나머지의 합
    return sum([i // 10 for i in memo])  # 각 쿠폰의 상황에서 시켜먹을 수 있는 치킨의 합

print(solution(chicken))
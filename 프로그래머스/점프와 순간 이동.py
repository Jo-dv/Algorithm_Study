n = 6

def solution(n):
    ans = 1  # 점프를 위해서라도 무조건 1만큼을 걸어야 함
    while n > 0:
        ans += n % 2  # 점프는 무조건 배수만큼 늘어나므로 n이 홀수일 때 나오는 나머지가 걸어간 거리가 됨
        n //= 2  # 점프
    return ans

print(solution(n))
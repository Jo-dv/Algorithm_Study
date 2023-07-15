from sys import stdin

n = int(stdin.readline().rstrip())
m = int(input())
malfunction = list(input().split()) if m != 0 else []  # 고장난 버튼이 없을 수도 있음
answer = abs(100 - n)  # 현재 채널에서 순수 + 또는 -를 눌러 변경한 경우

for i in range(1000001):  # 작은 값에서 목표값, 큰 값에서 목표값, 각각 50000번씩 접근
    for j in str(i):  # 숫자를 문자열로 바꿔 하나씩 쪼개서
        if j in malfunction:  # 하나라도 고장난 버튼을 누르려고 한다면
            break  # 종료하고 다음 값으로
    else:  # 문제없이 종료됐다면
        answer = min(answer, len(str(i)) + abs(i - n))  # +-를 누른 경우 혹은 숫자와 +-를 누른 경우가 횟수가 현재 횟수보다 작다면
print(answer)

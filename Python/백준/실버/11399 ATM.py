n = int(input())
p = sorted(map(int, input().split()))
time = [0]
answer = 0

for i in p:  # 정렬하여 적은 대기 시간순으로 누적합 계산
    time.append(time[-1] + i)
    answer += time[-1]

print(answer)
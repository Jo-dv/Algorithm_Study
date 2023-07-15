'''
for t in range(1, int(input())+1):  # 만들어 놓은 빵은 고려하지 않고 생산량만 고려한 문제
    n, m, k = map(int, input().split())
    waiting = list(map(int, input().split()))
    waiting.sort()

    if m <= waiting[0] and (waiting[-1] // m) * k >= n:  # 마지막으로 도착한 손님의 시간을 기준으로 만들어진 빵이 전체 손님보다 많으면
        print(f'#{t} Possible')  # 해당 조건은 중간에 빵이 없어서 못 받는 경우를 고려하지 못함
    else:
        print(f'#{t} Impossible')
'''


for t in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    waiting = list(map(int, input().split()))
    waiting.sort()

    for i in range(1, n+1):
        fish = (waiting[i-1] // m) * k  # 현재 손님의 도착 시간 기준으로 만들어지는 빵의 최대 개수를 갱신
        if fish < i:  # 갱신된 빵이 적어 i번째 사람이 받지 못하면
            print(f'#{t} Impossible')
            break
    else:  # 빵이 부족하지 않아서 모든 사람에게 정상적으로 팔았다면
        print(f'#{t} Possible')

# 1
# 5 2 3
# 2 2 2 2 4의 경우를 고려해 볼 것
k, s, n = input().split()
answer = []

d = {'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0),  # 구현, 시뮬레이션은 좌표계를 생각하여 이동에 대한 것을 매핑할 것
     'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)}

ky, kx = (int(k[1]) - 8) * -1, ord(k[0])-65  # 체스판의 위치를 좌표로 매핑, 좌측상단: (0, 0) ~ 우측하단: (7, 7)
sy, sx = (int(s[1]) - 8) * -1, ord(s[0])-65

for _ in range(int(n)):
    cmd = input()
    my, mx = d[cmd]
    if ky + my <= -1 or ky + my >= 8 or kx + mx <= -1 or kx + mx >= 8:  # 킹의 이동할 위치가 체스판을 벗어나면
        continue
    if ky + my == sy and kx + mx == sx:  # 킹이 이동할 위치에 돌이 있다면
        if sy + my <= -1 or sy + my >= 8 or sx + mx <= -1 or sx + mx >= 8:  # 돌을 먼저 이동시키는데
            continue  # 이동시킬 돌의 위치가 체스판을 벗어나면 둘의 이동을 수행하지 않음
        sy += my  # 벗어나지 않으면 돌 위치 이동
        sx += mx
    ky += my  # 범위를 벗어나지 않고 만약 돌이 이동 경로에 있는 상태에서 문제도 해결되었다면 킹 위치 이동
    kx += mx

print(chr(kx + 65) + str((ky - 8) * -1))  # 다시 원래의 체스판의 위치로 변환
print(chr(sx + 65) + str((sy - 8) * -1))
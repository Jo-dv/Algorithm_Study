t = int(input())

for i in range(1, t+1):
    n = int(input())
    answer = 0
    
    for y in range(1, n+1):  # 원점 기준, 수직 및 수평을 제외하고 1사분면에 대해 모든 점 탐색 = 유효성 검사
        for x in range(1, n+1):
            if x**2 + y**2 <= n**2:
                answer += 1
    answer *= 4  # 원은 대칭이므로 1사분명에서 얻은 점을 총 4사분면에 대해 갱신
    print(f'#{i} {answer + n * 4 + 1}')  # 제외한 부분의 점 + 원점의 점을 합산
    
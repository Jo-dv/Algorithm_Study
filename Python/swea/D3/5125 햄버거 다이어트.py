def dfs(score, calorie, idx):
    global ans
    if calorie > l:  # 칼로리를 임계를 넘어서면
        return  # ans를 갱신하지 않고 그대로 함수 종료
    if idx == n:  # 마지막까지 탐색했다면
        ans = max(ans, score)  # 현재 ans와 탐색이 종료된 시점의 score와 비교
        return
    dfs(score+arr[idx][0], calorie+arr[idx][1], idx+1)  # 해당 재료를 선택한 경우
    dfs(score, calorie, idx+1)  # 해당 재료를 선택하지 않은 경우

for i in range(1, int(input())+1):
    n, l = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0
    dfs(0, 0, 0)  # 점수, 칼로리, 첫 탐색 인덱스
    print(f'#{i} {ans}')

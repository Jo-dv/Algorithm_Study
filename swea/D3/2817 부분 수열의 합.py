def dfs(idx, check):
    global answer
    if check == k:  # 탐색 결과로 현재 값이 목표 k와 같다면
        answer += 1  # 경우의 수 갱신
        return
    if idx == n:  # 수열의 끝에 도달했다면 
        return  # 탐색 종료
    dfs(idx + 1, check + a[idx])  # 해당 인덱스의 값을 선택하고 다음 인덱스 탐색
    dfs(idx + 1, check)  # 해당 인덱스의 값을 선택하지 않고 다음 인덱스 탐색


for i in range(1, int(input())+1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    answer = 0
    dfs(0, 0)  # 초기 0번 인덱스, 합이 0인 상태로 탐색 시작
    print(f'#{i} {answer}')

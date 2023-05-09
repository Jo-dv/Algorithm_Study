'''
def dfs(idx, weight, value):  # 백트래킹을 이용한 접근 방법, 백트래킹의 시간 복잡도는 2^n, n <= 20일 때 적합
    global answer
    if idx == n or weight > k:  # 마지막 물건까지 탐색을 했거나, 현재 무게를 초과했을 경우
        return

    answer = max(answer, value)  # 현재 최적의 무게와 현재의 무게와 비교하여 값 갱신
    dfs(idx + 1, weight + items[idx][0], value + items[idx][1])  # 해당 인덱스의 아이템 선택
    dfs(idx + 1, weight, value)  # 해당 인덱스의 아이템 선택하지 않음


for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    answer = 0
    dfs(0, 0, 0)

    print(f'#{t} {answer}')'''

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    answer = [[0] * (k + 1) for _ in range(n + 1)]
    v, c = 0, 1

    for ni in range(1, n + 1):  # 각 아이템에 대해
        for ki in range(1, k + 1):  # 제한이 1 ~ K 까지일 때 최적의 값을 저장
            if items[ni - 1][v] > ki:  # 현재 선택된 아이템의 부피가 Ki의 부피를 가진 가방보다 크다면
                answer[ni][ki] = answer[ni - 1][ki]  # 직전에 값을 그대로 저장
            else:  # 만약 그렇지 않고 담을 수 있다면
                answer[ni][ki] = max(answer[ni - 1][ki], answer[ni - 1][ki - items[ni - 1][v]] + items[ni - 1][c])
                # answer[ni - 1][ki]: ni번째 아이템을 선택하지 않은 경우
                # ki - items[ni - 1][v]: 현재 무게에서 선택된 아이템의 무게를 뺐을 때 들어있는 가치
                # items[ni - 1][c]: 선택한 아이템의 가치
    print(f'#{t} {answer[-1][-1]}')

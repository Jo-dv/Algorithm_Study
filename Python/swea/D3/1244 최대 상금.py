from collections import deque

def bfs(num, k):
    max_num = -1  # 초기 최대값
    visited = [(num, k)]  # 현재 값과 교환 횟수를 저장
    q = deque([(num, k)])
    while q:
        cur, cnt = q.popleft()
        if cnt == 0:  # 교환 횟수를 다 사용했다면
            max_num = max(max_num, cur)  # 현재 최대값과 교환이 끝난 값을 비교해서 최댓값 갱신
            continue  # 다음 탐색으로 이동
        for i in range(len(str(cur))-1):  # 기준 노드
            for j in range(i+1, len(str(cur))):  # 비교 노드
                lst = list(str(cur))  # 정수 값을 문자열로 바꾼 후 스왑을 위해 리스트로 변환
                lst[i], lst[j] = lst[j], lst[i]  # 비교하면서 무조건 스왑
                new_num = int(''.join(lst))  # 스왑한 리스트를 다시 정수로 변환
                if (new_num, cnt-1) not in visited:  # 남은 교환 횟수와 그 횟수일 때 정수값이 아직 비교하지 않은 것이라면
                    visited.append((new_num, cnt-1))  # 저장
                    q.append((new_num, cnt-1))  # 그 후 그 값을 기준으로 탐색하기 위해 큐에 저장
    return max_num  # 모든 탐색이 끝난 후 최대값 반환

t = int(input())
for i in range(1, t+1):
    num, k = input().split()
    ans = bfs(int(num), int(k))  # 모든 경우의 수에 대해 중복없이 탐색을 위해 bfs 사용
    print(f"#{i} {ans}")
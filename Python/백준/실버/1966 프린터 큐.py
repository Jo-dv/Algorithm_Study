from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    ranks = list(map(int, input().split()))
    q = deque([(rank, doc_num) for doc_num, rank in enumerate(ranks)])  # 우선순위를 가진 문서들 생성
    priority = max(q)  # 현재 최고 우선순위
    answer = 0

    while q:
        if q[0][0] != priority[0]:  # 큐의 맨 앞 문서의 우선순위가 뽑아야할 우선 순위가 아니라면
            q.append(q.popleft())  # 뒤로 보냄
        else:
            answer += 1  # 출력 횟수 갱신
            if q.popleft()[1] == m:  # 큐에서 제거하고, 제거한 문서가 내가 알고자하는 문서라면
                break  # 탐색 종료
            priority = max(q)  # 아니라면 우선 순위 갱신

    print(answer)
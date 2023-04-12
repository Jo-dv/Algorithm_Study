from collections import deque

n, k = map(int, input().split())
q = deque(i+1 for i in range(n))
answer = []

for _ in range(n):
    q.rotate(-(k-1))  # 음수는 앞에서 뒤로, k-1번째 회전하면 제거할 k번째 값이 맨 앞에 위치하게 됨
    answer.append(q.popleft())

print(f'<{str(answer)[1:-1]}>')
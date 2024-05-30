from itertools import combinations as comb
from collections import deque, defaultdict
import math

def bfs(network, v):  # 일반 bfs
    dq = deque([v])
    visited = {v}
    
    while dq:
        node = dq.popleft()

        for i in network[node]:
            if i not in visited:
                visited.add(i)
                dq.append(i)

    return len(visited)

def solution(n, wires):
    answer = math.inf
    
    for i in wires:  # wire 기준으로 전력망 분리
        network = defaultdict(list)

        for j in wires:  # 전력망 분리 단계
            if i != j:  # 기준 전력망을 제외하고
                network[j[0]].append(j[1])  # 그래프 생성
                network[j[1]].append(j[0])
        
        v1_len = bfs(network, i[0])  # wire 기준으로 탐색
        v2_len = bfs(network, i[1])

        answer = min(answer, abs(v1_len - v2_len))

    return answer

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting = deque(truck_weights)
    bridge = deque(0 for _ in range(bridge_length))
    wait_sum = 0

    while waiting:  # 다리를 지나야 하는 트럭이 남아있다면
        wait_sum -= bridge.popleft()  # 다리의 맨 앞이 트럭이라면 빠져나와야 함
        if wait_sum + waiting[0] > weight:  # 현재 다리에 실린 무게와 앞으로 들어올 트럭의 무게의 합이 초과될 경우
            bridge.append(0)  # 다리의 길이를 맞춰주기 위해 0 추가
        else:  # 초과되지 않는다면
            x = waiting.popleft()  # 대기중인 트럭을 빼서
            wait_sum += x  # 무게 추가
            bridge.append(x)  # 다리 추가
        answer += 1  # 모든 동작이 끝나면 항상 1초가 소요

    answer += bridge_length  # 다리에 남은 트럭들이 다리를 빠져나가는 시간은 다리의 길이만큼 소요됨
    return answer

bridge_length, weight, truck_weights = 10, 12, [4, 4, 4, 2, 2, 1, 1, 1, 1]

print(solution(bridge_length, weight, truck_weights))
from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]


def solution(bridge_length, weight, truck_weights):
    answer = 0
    wait_truck = deque(truck_weights)
    passing_truck = deque(maxlen=bridge_length)
    passed_truck = []


    while wait_truck:
        if sum(passing_truck) > weight:
            passed_truck.append(passing_truck.popleft())
            answer += bridge_length
        else:
            passing_truck.append(wait_truck.popleft())
            answer += 1

    return answer


print(solution(bridge_length, weight, truck_weights))

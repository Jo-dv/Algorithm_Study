def solution(friends, gifts):
    answer = 0

    return answer
'''
1. 두 사람 사이에 선물을 주고 받은 기록이 있다면 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 받음
2. 기록이 없거나 같다면 선물 지수가 더 큰 사람이 받음
2-1. 선물 지수 = 이번 달까지 친구들에게 준 선물의 수 - 지금까지 받은 선물의 수
2-2. 서로의 선물 지수가 0이라면 b가 a에게 받음
2-3. 서로의 선물 지수가 0이 아닌 수로 선물 지수가 같다면 아무에게도 선물을 주지 않음
3. 선물을 가장 많이 받은 사람의 선물 수
'''

friends, gifts = ["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
print(solution(friends, gifts))
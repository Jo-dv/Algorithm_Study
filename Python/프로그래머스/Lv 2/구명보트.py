from collections import deque

people = [70, 20, 50, 80, 30, 50, 60, 30]
limit = 100

def solution(people, limit):
    boat = []
    people.sort()  # 그리디 문제 해결을 위한 아이디어, 몸무게별로 정렬
    people = deque(people)  # sorted()를 쓸 경우 .sort()보다 느림

    while people:  # 구해야 할 사람들이 남아있을 때까지
        if people[0] > limit // 2:  # 첫 단이 limit보다 크다면 모두 한 번씩 밖에 태울 수 없음
            return len(people) + len(boat)  # 그래서 보트에 탑승한 사람 + 남은 사람
        elif len(people) > 1 and people[0] + people[-1] <= limit:  # 남은 사람이 2명 이상, 양 끝단의 몸무게 합이 limit이하라면
            boat.append(people.popleft() + people.pop())  # 양쪽에서 pop하여 보트에 태움, 결과적으로 항상 2명을 태우게 됨
        else:  # 남은 사람이 2명 이상이긴 하지만 양 끝단의 뭄무게 합이 limit을 초과하는 경우. 가장 무거운 사람만 보트에 태움
            boat.append(people.pop())

    return len(boat)  # 배열의 길이 = 보트에 탑승한 사람

print(solution(people, limit))
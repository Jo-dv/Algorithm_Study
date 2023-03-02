from collections import deque

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

def solution(cacheSize, cities):
    answer = 0
    cache = deque(cacheSize)

    for i in cities:
        i = i.lower()
        if i not in cache:
            cache.appendleft(i)
            answer += 5
        else:
            cache.remove(i)
            cache.appendleft(i)
            answer += 1

    return answer

print(solution(cacheSize, cities))




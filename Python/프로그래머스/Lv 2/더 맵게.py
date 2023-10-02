import heapq

scoville = [0, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        if scoville[0] >= K:
            break

        x1 = heapq.heappop(scoville)
        x2 = heapq.heappop(scoville)
        heapq.heappush(scoville, x1 + x2 * 2)
        answer += 1

    return answer


print(solution(scoville, K))
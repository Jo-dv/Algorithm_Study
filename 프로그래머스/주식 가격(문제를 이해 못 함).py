prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(answer)):
        pivot = prices[i]
        for j in range(i + 1, len(prices)):
            if pivot <= prices[j]:
                answer[i] += 1

    return answer

print(solution(prices))
citations = [3, 0, 6, 1, 5]

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(1, len(citations) + 1):
        if i <= citations[i-1]:
            answer = i
    return answer

print(solution(citations))
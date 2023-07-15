numbers = [5, 0, 2, 7]
#result = [2,3,4,5,6,7]

def solution(numbers):
    numbers.sort()
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    answer = list(set(answer))
    answer.sort()
    return answer

print(solution(numbers))
'''
def solution(numbers):  # 앞에서부터 탐색, 느림
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):  # 기준 숫자보다
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:  # 큰 수가 나올 때까지 탐색
                answer[i] = numbers[j]
                break

    return answer

def solution(numbers):  # 인덱스 저장을 이용한 탐색, 가장 빠름
    answer = [-1] * len(numbers)
    s = []

    for i in range(len(numbers)):
        while s and numbers[s[-1]] < numbers[i]:  # 마지막 인덱스의 숫자보다 큰 값을 만나면
            answer[s.pop()] = numbers[i]  # 해당 인덱스를 제거하고 그 인덱스의 값은 발견한 큰 값으로 갱신, 스택의 저장된 모든 값을 비교
        s.append(i)  # 항상 인덱스 저장

    return answer
'''

def solution(numbers):  # 뒤에서부터 탐색, 빠름, 직관적
    answer = [-1] * len(numbers)
    
    for i in range(len(numbers) - 1, -1, -1):  # 기준 숫자보다
        for j in range(i - 1, -1, -1):
            if numbers[j] >= numbers[i]:  # 작은 수가 나올 때까지 탐색
                break
            answer[j] = numbers[i]  # 탐색된 숫자가 기존 숫자보다 작으면 해당 숫자를 기준 숫자로 치환
    return answer


numbers = [2, 3, 3, 5]

print(solution(numbers))

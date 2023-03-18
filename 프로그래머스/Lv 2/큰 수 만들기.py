number, k = "4321", 1

def solution(number, k):
    answer = []
    for i in number:
        while answer and answer[-1] < i and 0 < k:  # 2. 값이 저장되어 있고 마지막으로 저장된 값이 현재 값보다 작고 뺄 횟수가 있다면
            answer.pop()  # 마지막 값을 빼고 더 큰 현재의 값으로 변경
            k -= 1  # 뺄 수 있는 횟수 차감
        answer.append(i)  # 1. 탐욕 알고리즘에 따라 일단 값을 저장

    return ''.join(answer) if k == 0 else ''.join(answer[:-k])  # 다 뺐으면 그대로 출력 아니라면 뺄 수 있는 횟수 만큼 뒤에서 절삭

print(solution(number, k))
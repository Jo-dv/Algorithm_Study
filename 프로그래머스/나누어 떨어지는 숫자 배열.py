arr = [5, 9, 7, 10]
divisor = 5

def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    answer.sort()
    if not answer:
        answer.append(-1)
    return

print(solution(arr, divisor))
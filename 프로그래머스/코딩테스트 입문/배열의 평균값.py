numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def solution(numbers):  # 누적합 배열 형태의 풀이 법
    d, t = [], 0

    for i in numbers:
        d.append(t + i)
        t = d[-1]
    return d[-1] / len(d)

print(solution(numbers))
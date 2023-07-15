n, left, right = 4, 7, 14

def ex_solution(n, left, right):  # 주어진 문제에 충실하게 풀 경우, 시간 초과 문제 발생
    matrix = [[j + 1 if j == i else 0 for j in range(n)] for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            matrix[i][j] = matrix[j][i] = i + 1

    answer = [j for i in matrix for j in i]
    return answer[left:right + 1]

def solution(n, left, right):
    answer = [(i % n)+1 if i % (n + 1) == 0 else 0 for i in range(left, right + 1)]  # 1차원 리스트 형태로 대각값 초기화

    for i in range(len(answer)):
        if not answer[i]:  # 대각값을 제외하고
            if (left % n)+1 > (left // n)+1:  # 대각선 기준 상단 삼각형 부분일 경우
                answer[i] = (left % n)+1
            else:  # 하단 삼각형 부분일 경우
                answer[i] = (left // n)+1
        left += 1
    
    # left 값의 몫과 나머지 값을 비교하면 나머지는 상단 삼각형이, 몫은 하단 삼각형의 값이 더 크다.
    return answer


print(solution(n, left, right))

dots = [[3, 5], [4, 1], [2, 4], [5, 10]]

def solution(dots):
    dots.sort()  # 단순 직선의 기울기 문제, 일반적으로 직선은 가까운 두 점끼리 연결하므로 크기순으로 정렬
    l1 = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
    l2 = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])
    return 1 if l1 == l2 else 0

print(solution(dots))
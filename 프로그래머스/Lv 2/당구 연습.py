def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:  # 각 방향에 대한 대칭이동 시 거리 계산, 치는 공 기준
        left = (startX + x)**2 + (startY - y)**2
        right = (startX - (2 * m - x))**2 + (startY - y)**2
        up = (startX - x)**2 + (startY - (2 * n - y))**2
        down = (startX - x)**2 + (startY + y)**2
        if startX == x:  # 수평 및 수직 위치에 나란히 있을 때 치는 공은 쳐야할 공쪽으로 갈 수 없음
            answer.append(min(left, right, down)) if startY < y else answer.append(min(left, right, up))
        elif startY == y:
            answer.append(min(left, up, down)) if startX < x else answer.append(min(right, up, down))
        else:  # 두 공이 대각을 이루고 있다면 모든 방향에 대해 계산
            answer.append(min(left, right, up, down))

    return answer
    # 피타고라스로 계산하려고 시도했으나 대각일 때 값을 구할 방법도 떠오르지 않고 값이 float이라 근사값으로 떨어지기 때문에 오차 발생 가능성 있음

m, n, startX, startY, balls = 10, 10, 5, 9, [[5, 8]]

print(solution(m, n, startX, startY, balls))

![그림1](https://user-images.githubusercontent.com/63555689/229997090-f306615c-032b-40a0-9aef-d2be2ded99ef.png)

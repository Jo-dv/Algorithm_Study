def check_move(pos, direction, distance, park, row_park):
    y, x = pos
    if direction == 'E':
        if x + distance <= len(park[0])-1 and 'X' not in park[y][x:x+distance+1]:  # +1을 하지 않으면 마지막 지점은 무시됨.
            x += distance
    elif direction == 'W':
        if x - distance >= 0 and 'X' not in park[y][x-distance:x]:
            x -= distance
    elif direction == 'S':
        if y + distance <= len(park)-1 and 'X' not in row_park[x][y:y+distance+1]:
            y += distance
    else:
        if y - distance >= 0 and 'X' not in row_park[x][y-distance:y]:
            y -= distance
    return y, x

def solution(park, routes):
    y, x = [(i, line.find('S'))for i, line in enumerate(park) if 'S' in line][0]  # 시작 위치 탐색, 결과는 튜플 형태의 원소 하나
    row_park = list(zip(*park))  # y에 대해 탐색할 데이터

    for i in routes:
        way, dis = i.split()  # 방향과 거리
        y, x = check_move((y, x), way, int(dis), park, row_park)  # 방향을 넘기지 않고 이동할 거리 내에 장애물이 없는지 확인
    return [y, x]


park, routes = ["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]

print(solution(park, routes))
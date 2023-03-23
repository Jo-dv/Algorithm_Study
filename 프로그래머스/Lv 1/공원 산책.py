def solution(park, routes):
    H, W = len(park)-1, len(park[0])-1
    y, x = [(i, line.find('S')) for i, line in enumerate(park) if 'S' in line][0]  # 시작 위치 탐색, 결과는 튜플 형태의 원소 하나
    row_park = list(zip(*park))  # y에 대해 탐색할 데이터

    for i in routes:
        way, dis = i.split()  # 방향과 거리, # 방향을 넘기지 않고 이동할 거리 내에 장애물이 없다면
        if way == 'E':
            if x + int(dis) <= W and 'X' not in park[y][x:x+int(dis)+1]:  # +1을 하지 않으면 마지막 지점은 무시된다.
                x += int(dis)
        elif way == 'W':
            if 0 <= x - int(dis) and 'X' not in park[y][x-int(dis):x]:
                x -= int(dis)
        elif way == 'S':
            if y + int(dis) <= H and 'X' not in row_park[x][y:y+int(dis)+1]:
                y += int(dis)
        else:
            if 0 <= y - int(dis) and 'X' not in row_park[x][y-int(dis):y]:
                y -= int(dis)
    return [y, x]

park, routes = 	["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]

print(solution(park, routes))
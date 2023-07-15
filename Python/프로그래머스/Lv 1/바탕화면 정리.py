wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]

def solution(wallpaper):
    check = []
    for col, i in enumerate(wallpaper):
        for row, j in enumerate(i):
            if j != '#':
                continue
            check.append((col, row))  # 최초로 파일을 만나면 해당 좌표 저장
    min_y, min_x = min(check)[0], min(check, key=lambda x: x[1])[1]
    max_y, max_x = max(check)[0]+1, max(check, key=lambda x: x[1])[1]+1
    return [min_y, min_x, max_y, max_x]
    # 시작 드래그 위치는 파일의 좌표 중, y의 최소, x의 최로 구성, 마지막 드래그 위치는 y의 최대+1, x의 최대+1

print(solution(wallpaper))
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

n = len(arr)

arr2 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]


def rotate(cnt):
    global arr
    for _ in range(cnt):
        temp = [i[:] for i in arr]
        for x in range(n):
            for y in range(n):
                temp[y][x] = arr[n - x - 1][y]
        arr = temp

    for i in arr:
        print(i)


def rotate2(sy, sx, size, cnt):
    global arr
    for _ in range(cnt):
        temp = [i[:] for i in arr]
        for y in range(sy, sy + size):
            for x in range(sx, sx + size):
                oy, ox = y - sy, x - sx
                ry, rx = ox, size - oy - 1
                temp[sy + ry][sx + rx] = arr[y][x]
        arr = temp

    for i in arr:
        print(i)


# rotate(3)
# 1: 시계 방향 90 = 반시계 방향 270
# 2: 시계 방향 180 = 반시계 방향 180
# 3: 시계 방향 270 = 반시계 방향 90

# rotate2(2, 2, 2, 3)

def rotate3(cnt):
    global arr2
    rows, cols = len(arr2), len(arr2[0])  # 초기 배열의 행과 열 크기 확인
    for _ in range(cnt % 4):  # 4번 회전하면 원래 모양으로 돌아오므로, cnt를 4로 나눈 나머지만큼 회전
        temp = [[0] * rows for _ in range(cols)]
        for x in range(rows):
            for y in range(cols):
                temp[y][rows - 1 - x] = arr2[x][y]
        arr2 = temp
        rows, cols = len(arr2), len(arr2[0])

    for row in arr2:
        print(row)


rotate3(3)


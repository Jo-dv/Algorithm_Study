T = int(input())

for i in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]  # 스도쿠 생성
    t_sudoku = [list(i) for i in zip(*sudoku)]  # 열을 검사하기 위한 전치 스토쿠
    grid = []  # 3 x 3 격자를 검사하기 위한 list

    for j in range(3):  # 검사할 층
        for col in range(3):  # 열을 검사
            flatten = []
            for row in range(3):  # 행을 검사
                flatten.extend(sudoku[row + j*3][col*3:col*3 + 3])  # 격자를 한 줄로 펼침
                grid.append(flatten)
                '''결과적으로 스도쿠를 3 x 3의 격자 9개로 나누고 다음과 같은 순서로 flatten을 수행
                   [1, 2, 3,
                    4, 5, 6,
                    7, 8, 9]'''

    for j, k, l in zip(sudoku, t_sudoku, grid):  # row, column, flatten을 한 줄씩 가져옴
        if sorted(j) == sorted(k) == sorted(l) == list(range(1, 10)):  # 각 줄을 정렬하여 [1 .. 9]와 같다면
            continue  # 다음 줄 검사
        else:  # 하나라도 같지 않다면
            print(f'#{i} 0')  # 해당 스도쿠는 적합하지 않음
            break  # 반복 강제 종료
    else:  # for가 정상적으로 종료되었다면
        print(f'#{i} 1')  # 해당 스도쿠는 적합함

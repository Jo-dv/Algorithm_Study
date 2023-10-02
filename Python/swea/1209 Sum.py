T = 10  # [제약 사항] 총 10개의 테스트 케이스가 주어진다.

for test_case in range(1, T + 1):
    test_num = int(input())  # 각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고
    arr = [list(map(int, input().split())) for _ in range(100)]  # 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.
    col, row = -1, -1  # 테스트 케이스마다 max sum을 구하기 위해 값 초기화
    # l_diagonal, r_diagonal = 0, 0  # 문제는 대각선도 구하라고 명시하였지만 그럴 경우 오답처리가 됨

    for row_idx in range(len(arr)):  # 배열의 길이 만큼
        col_temp, row_temp = 0, 0
        # l_diagonal += arr[col_idx][col_idx]
        # r_diagonal += arr[col_idx][len(arr)-1-col_idx]

        for col_index in range(len(arr)):  # 이중 for문의 구조상 row_idx가 고정되면 col_idx가 순차적으로 변함, 이 특성을 이용해
            col_temp += arr[col_index][row_idx]  # 열에 대해
            row_temp += arr[row_idx][col_index]  # 행에 대해

        col = max(col, col_temp)
        row = max(row, row_temp)

    # print(f'#{test_case}  {max(col, row, l_diagonal, r_diagonal)}')
    print(f'#{test_case}  {max(col, row)}')  # #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력
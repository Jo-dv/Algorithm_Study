land = [[9, 9, 9], [10, 7, 2]]

def solution(land):
    '''
    for row in range(1, len(land)):  # 주어진 문제에 대해: 열 4개짜리
        land[row][0] += max(land[row-1][1], land[row-1][2], land[row-1][3])
        land[row][1] += max(land[row-1][0], land[row-1][2], land[row-1][3])
        land[row][2] += max(land[row-1][0], land[row-1][1], land[row-1][3])
        land[row][3] += max(land[row-1][0], land[row-1][1], land[row-1][2])
    '''
    # 히든 테스트케이스 존재, 열 3개짜리 -> 열에 상관없는 일반화된 풀이 필요
    for row in range(1, len(land)):
        for col in range(len(land[0])):
            land[row][col] += max(land[row-1][:col] + land[row-1][col+1:])  # 슬라이싱된 리스트를 결합
            # 인덱싱의 경우 범위를 초과하면 에러가 발생하지만 슬라이싱의 경우 발생하지 않음

    return max(land[-1])

print(solution(land))
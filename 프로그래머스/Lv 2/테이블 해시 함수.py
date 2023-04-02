from functools import reduce

def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))  # 주어진 조건대로 정렬
    cal = [sum([j % (i+1) for j in data[i]]) for i in range(row_begin-1, row_end)]  # 주어진 조건대로 합 정의
    # 문제에서 낚였던 점은 2개의 데이터가 아닌 begin부터 end까지의 데이터임
    return reduce(lambda x, y: x ^ y, cal)  # 누적 xor 연산, 문제의 관건은 ^을 알고있냐 아니냐 싸움

'''
def solution(data, col, row_begin, row_end):  # reduce 안 쓰면 다음 코드처럼 누적값 표현
    data.sort(key=lambda x: (x[col-1], -x[0]))
    cal = [sum([j % (i+1) for j in data[i]]) for i in range(row_begin-1, row_end)]
    answer = cal[0]
    for i in range(1, len(cal)):
        answer ^= cal[i]

    return answer
'''

data, col, row_begin, row_end = [[2, 2, 6],
                                 [1, 5, 10],
                                 [4, 2, 9],
                                 [3, 8, 3]], 2, 2, 3

print(solution(data, col, row_begin, row_end))
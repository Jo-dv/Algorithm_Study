score = [[1, 2], [1, 1], [1, 1]]

def solution(score):
    avg = sorted([sum(i)/2 for i in score], reverse=True)
    return [avg.index(sum(i)/2)+1 for i in score]  # 값이 중복될 때, 인덱스는 선두의 인덱스가 반환

print(solution(score))
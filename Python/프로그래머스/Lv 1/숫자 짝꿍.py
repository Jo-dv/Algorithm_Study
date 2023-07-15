X, Y = "100", "2345"

def solution(X, Y):
    answer = ''.join([str(i)*min(X.count(str(i)), Y.count(str(i))) for i in range(9, -1, -1)])  
    # 9부터 인덱싱하여 큰순으로 비교
    # 개수의 최소는 공통 개수를 의미
    return answer if any(i != '0' for i in answer) else '-1' if answer == '' else '0'
    # 문자열 모두가 0이 아니라면 그대로 반환, 그렇지 않고 빈 문자열이면 -1, 모두 0으로 이루어져 있으면 0 반환

print(solution(X, Y))
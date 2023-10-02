common = [1, 3, 9]

def solution(common):
    check = [i - j for i, j in zip(common[1:], common[:-1])]  # 짝수 번째 값에서 홀수 번째 값의 차이를 구함
    return common[-1] + check[-1] if check[1:] == check[:-1] else common[-1] * check[1] // check[0]
    # 등차라면 check에 모든 값이 동일할 것이며 그 값은 공차
    # 그렇지 않으면 원소의 수는 최소 3이므로 두 번째 값에서 첫 번째 값을 나눠 등비를 구함

print(solution(common))
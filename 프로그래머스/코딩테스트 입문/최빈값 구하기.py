array = [1, 2, 3, 3, 3, 5, 5, 4]

def solution(array):
    dic = {i: 0 for i in sorted(array)}  # 키 값 리스트 생성
    for i in array:  # 빈도 체크
        dic[i] += 1
    dic[-1] = 0  # 더미 값 삽입, 원 배열의 길이가 1일 때 오류를 방지하기 위함

    a = sorted(list(dic.items()), key=lambda x: x[1], reverse=True)  # 숫자와 빈도를 집합으로 하는 리스트, 빈도가 큰 순으로 정렬

    answer = a[0][0] if a[0][1] != a[1][1] else -1  # 첫 값과 다음 값이 다르다면 최빈값은 고유값이므로 첫 값의 빈도 반환 아니라면 -1

    return answer

print(solution(array))


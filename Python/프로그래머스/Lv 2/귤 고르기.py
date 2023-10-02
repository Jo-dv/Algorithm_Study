k, tangerine = 6, [1, 3, 2, 5, 4, 5, 2, 3]

def solution(k, tangerine):
    answer, dic = 0, {i: 0 for i in set(tangerine)}  
    for i in tangerine:  # 귤의 종류별 개수 카운팅
        dic[i] += 1

    dic = sorted(list(dic.values()), reverse=True)  # 종류가 많은 순으로 정렬
    for i in dic:
        if k > 0:  # 담을 수 있을 때까지
            answer += 1  # 귤의 종류 추가
            k -= min(i, k)  # 담은 개수만큼 감산
            # min은 안 해줘도 되는데 상식적으로 {3: 5, 1: 3}, k = 6일 경우 i를 그대로 빼면 k = -2가 되기에 이치에 맞지 않아서 했음
    return answer

print(solution(k, tangerine))
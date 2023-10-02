from math import inf

def changer(arr, op):
    answer = inf if op == 0 else -inf
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            temp = arr.copy()  # 옅은 복사를 하면 다음 반복 때, 변경된 값이 그대로 사용되므로 매번 비교할 때마다 깊은 복사로 원본 복사
            temp[i], temp[j] = temp[j], temp[i]
            if op == 0:  # 최소
                if len(n) > 1:  # 길이가 1보다 크다면
                    if temp[0] != '0':  # 앞이 0이 오는 경우를 제외하고
                        answer = min(answer, int(''.join(temp)))  # 현재 값과 변경된 값을 비교해서 작은 값으로 갱신
                else:  # 길이가 1이라면 0 ~ 9사이의 값이고 전부 -inf보다 크기 때문에 단일 값을 정수로 변환
                    answer = int(temp[0])
            else:  # 최대
                answer = max(answer, int(''.join(temp)))
    return answer

for t in range(1, int(input())+1):
    n = list(input())
    print(f'#{t} {changer(n, 0)} {changer(n, 1)}')

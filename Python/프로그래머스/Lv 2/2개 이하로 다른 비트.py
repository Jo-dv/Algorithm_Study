numbers = [0, 343, 1015]


def solution(numbers):
    answer = []

    for i in numbers:
        if i % 2 == 0:  # 짝수일 경우 
            answer.append(i+1)  # 다음 수와 비트이 차이는 무조건 1
        else:
            val = bin(i)[2:]
            if '0' not in val:  # 2의 배수 -1일 경우 모든 자리가 1인 홀수일 경우
                answer.append(int(val, 2) + 2**(len(val)-1))  # 조건에 부합하는 다음 값은 현재 값 + 2^(현재 비트의 길이-1)
            else:
                for j in range(len(val)-1, -1, -1):  # 그게 아닌 홀수일 경우, 오른쪽에서부터 탐색하여
                    if val[j] == '0':  # 0이 나온 경우, 그 값과 그 이전 값을 반대 값으로 전환(결과적으로 1과 0이 됨)
                        answer.append(int(val[:j] + '10' + val[j+2:], 2))
                        break  # 해당 값에 대한 정답을 찾으면 다음 수로 넘어감

    return answer

print(solution(numbers))
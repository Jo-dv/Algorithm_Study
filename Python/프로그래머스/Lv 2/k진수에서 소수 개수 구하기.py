def solution(n, k):
    answer = 0
    notation = ''

    while n > 0:  # 진수 변환
        notation += str(n % k)
        n //= k

    for i in notation[::-1].split('0'):  # 변환된 진수를 0으로 분리, 문제의 조건을 따져보면 결국 0이 없는 경우임
        if i == '' or int(i) < 2:  # 0은 공백처리이므로 먼저 검사, 공백이거나 1이면 다음으로 넘어감
            continue
        for j in range(2, int(int(i) ** 0.5) + 1):  # i를 2부터 i의 제곱근까지 나눠보고 나눠지는 수가 있다면 소수가 아니므로 종료
            if int(i) % j == 0:
                break
        else:
            answer += 1  # 종료되지 않았다는 것은 나눠지는 수가 없었다는 의미이므로 소수

    return answer

n, k = 3, 3

print(solution(n, k))
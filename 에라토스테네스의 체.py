n = 10

def solution1(n):
    temp = [True for _ in range(n + 1)]
    # 정수를 표현하기 위한 리스트로 1부터 표현하기 위해 +1, 인덱스 번호 = 정수, 초기엔 모두 실수라고 가정
    # 2 ~ N까지 모든 자연수를 나열

    for i in range(2, int(n**0.5) + 1): # 1은 소수가 아니므로 실질적인 범위인 2부터 시작
        # 불필요한 계산을 수행하지 않도록 n의 제곱근까지만 계산, 제곱근을 기준으로 대칭이 전환되므로 실질적으로 반복적인 계산이 발생
        if temp[i]: # True 경우
            j = 2
            while i * j <= n: # 계산된 값이 주어진 범위 안이라면 계속해서 계산
                temp[i * j] = False # i의 배수를 제거, 단 i는 제거하지 않는다.
                j += 1
    answer = [i for i in temp[2:] if i] # 실수라고 판정된 것들만 추려냄, # 0과 1을 별도의 조정을 가하지 않았기 때문에 True로 표현
    return len(answer) # 배열의 길이 -> 주어진 수보다 작은 소수들의 수

def solution2(n):
    temp = [True for _ in range(n+1)]

    for i in range(2, n+1):
        if not i:
            continue
        for j in range(i**2, n+1, i):
            temp[j] = False

    answer = [i for i in temp[2:] if i]
    return len(answer)

def solution3(n):  # 1과 2의 특징을 조합 -> 가장 빠름, 솔루션 1에서 2배 정도 속도 개선
    temp = [True for _ in range(n + 1)]

    for i in range(2, int(n**0.5) + 1):
        if temp[i]:
            for j in range(i**2, n+1, i):
                temp[j] = False
                
    answer = [i for i in temp[2:] if i]
    return len(answer)

print(solution1(n))
print(solution2(n))
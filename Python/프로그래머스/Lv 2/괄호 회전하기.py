s = '}]()[{'

def check(s):
    temp, dict = [], {']': '[', ')': '(', '}': '{'}

    while s:
        if s[0] in dict.values():  # 맨 앞의 원소가 시작하는 기호라면
            temp.append(s.pop(0))  # 뽑아서 비교를 위한 임시 리스트에 저장
            continue  # 닫는 기호가 나올 때까지 해당 과정 반복
        if temp and temp[-1] == dict[s[0]]:  # 맨 앞의 원소가 닫는 원소이고 임시 리스트에 값이 있고 그것이 마지막 기호와 짝이라면
            temp.pop()
            s.pop(0)
            continue  # 둘 다 리스트에서 제거, 아래 break문을 실행하지 않기 위해 continue
        break  # 닫는 원소로 시작하면 검사 종료
    return not (s or temp)  # nor의 성질을 이용하여 둘 다 비어있을 때 True를 반환, 둘 다 비어있다는 것은 올바른 문자열이라는 뜻

def solution(s):  # deque을 쓰나 안 쓰나 시간 복잡도는 동일함
    answer = 0
    s = list(s)
    for _ in range(len(s)):  # s의 길이만큼
        s.append(s.pop(0))  # 맨 앞의 원소를 맨 뒤로 보냄
        answer += 1 if check(s.copy()) else 0  # s의 객체를 복사하지 않고 s 자체를 전달하면 check에서 s에 영향을 줌
    return answer

print(solution(s))
numbers = 'onetwothreefourfivesixseveneightnine'

def solution(numbers):
    check = dict(zip(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], range(10)))
    t, answer = '', ''
    for i in numbers:  # 왼쪽부터 시작해서 문자 탐색
        t += i
        if t in check:  # 탐색되어서 만들어진 단어가 있다면
            answer += str(check[t])  # 해당 단어의 번호를 저장
            t = ''  # 탐색 결과 초기화

    return int(answer)

print(solution(numbers))
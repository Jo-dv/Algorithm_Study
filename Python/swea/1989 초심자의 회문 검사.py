T = int(input())

for i in range(1, T+1):
    problem = input()
    answer = 0

    for j in range(1, len(problem)//2+1):  # 중간 문자까지
        if problem[j-1] == problem[-j]:  # 양 끝단을 비교하면서 범위 축소
            continue  # 짝이 맞다면 다음 문자 검사를 위해 continue
        else:  # 짝이 맞지 않는다면
            break  # 반복 중단
    else:  # 반복문이 중단되지 않고 종료되었다는 것은 break가 발생하지 않았다는 뜻, 즉 회문
        answer = 1
    print(f'#{i} {answer}')
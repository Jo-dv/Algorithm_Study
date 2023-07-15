for t in range(1, int(input())+1):  # 주어진 순열로 만들 수 있는 값을 다시 하나의 순열로 봤을 때 해당 순열이 단조 증가인지 확인하는 문제
    n = int(input())
    a = list(map(int, input().split()))
    answer = -1  # for else를 사용하여 반복을 종료하기 때문에 비정상적인 종료를 대비해 처음부터 -1로 초기화

    for i in range(n - 1):  
        for j in range(i + 1, n):
            temp_int = a[i] * a[j]  # Ai x Aj 계산
            temp = str(temp_int)  # 순열의 값은 한 자리의 수이므로 굳이 정수형 리스트로 변환할 필요 없음. 문자열일 경우 순위가 값이므로
            # 정수형 리스트로 변환하면 시간이 더 많이 걸림
            # list(map(int, str(temp_int))): O(N)
            # str(temp_int): O(log N)  둘 다 N은 자릿수를 의미 자릿수가 길어질수록 str 변환이 더 유리
            for ki, kj in zip(temp[:-1], temp[1:]):  # 해당 순열에서 인접한 값들을 비교하며
                if ki > kj:  # 단조 증가하지 않으면
                    break  # 종료
            else:  # 정상적으로 반복이 종료되면
                answer = max(answer, temp_int)  # 역대 계산된 값을 갱신

    print(f'#{t} {answer}')

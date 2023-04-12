for _ in range(int(input())):  # 재귀로 풀면 시간 초과 발생
    n = int(input())

    answer = [(1, 0), (0, 1)]  # 0과 1의 값이 아닌 호출 횟수를 저장, (zeros, ones)
    for i in range(2, n+1):  # dp 풀이
        zeros = answer[-1][0] + answer[-2][0]
        ones = answer[-1][1] + answer[-2][1]
        answer.append((zeros, ones))

    print(*answer[-1]) if n != 0 else print(*answer[0])
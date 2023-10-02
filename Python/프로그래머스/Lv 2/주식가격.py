prices = [1, 2, 3, 2, 3]

'''
def solution(prices):  # 내가 현재 시점에서 산 주식이 다음에 산 주식들과 비교했을 때 얼마나 버티는지 계산하는 문제
    answer = [0] * len(prices)  # 모든 주식에 대해 카운팅하며 append가 아니라 값을 갱신할 것이고 마지막은 어차피 0이기 때문에

    for i in range(len(answer)):
        current = prices[i]  # 현재 시점의 가격 저장, 굳이 저장할 필요는 없음
        for j in range(i + 1, len(prices)):  # 이후 시점부터 마지막까지
            answer[i] += 1  # 일단 구매 시점에서 무조건 1초
            if current > prices[j]:  # 하락했다면 탐색 종료
                break

    return answer'''

def solution(prices):  # 스택을 이용한 풀이
    stack, answer = [], [0] * len(prices)
    append, pop = stack.append, stack.pop

    for now in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[now]:  # 스택에 값이 있고 마지막 값의 가격이 현재 가격보다 클 경우 -> 가격의 하락
            past = pop()[0]  # 마지막 값의 시점을 가져와서
            answer[past] = now - past  # 지금까지의 시간과의 차만큼을 가지고 시점 갱신
        append([now, prices[now]])  # i 시점의 가격 저장
        # 저장된 값은 시세의 하락 없이 계속해서 유지 및 상승했다는 것

    for time, _ in stack:  # 저장된 시세 정보, 즉 하락하지 않은 주식들의 시세 정보를 바탕으로
        answer[time] = (len(prices) - 1) - time  # 시점의 시작은 길이-1부터 시작하고 여기서 자신의 시간을 빼면 유지 시간이 됨

    return answer

print(solution(prices))
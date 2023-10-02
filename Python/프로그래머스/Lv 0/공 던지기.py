numbers, k = [1, 2, 3, 4, 5], 3

def solution(numbers, k):
    return (k-1) * 2 % len(numbers) + 1
    # 공은 현재 사람에서 + 2 위치에 해당하는 사람이므로 2k이며 여기서 총인원으로 나누면 자신의 번호가 됨
    # k-1은 k번째 사람 바로 앞 사람이며 k에서 총 인원으로 나눌 경우 k와 인원의 수가 같다면 자신의 번호가 아닌 0이 되기에 앞 사람에서 나누고 1을 더해줌
print(solution(numbers, k))
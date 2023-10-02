from collections import deque

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    r = [int(input()) for _ in range(n)]  # 주차 공간별 요금
    w = {i: int(input()) for i in range(1, m + 1)}  # 차량별 무게
    enter_info = deque([int(input()) for _ in range(2 * m)])  # 출입 기록
    parking = [False] * n  # 주차장
    parking_num = n  # 남은 주차 공간
    waiting = deque([])  # 대기 정보
    answer = 0

    while enter_info:  # 출입 기록에 대한 처리가 끝날 때까지
        car = enter_info.popleft()  # 맨 앞에서 부터 처리

        if waiting:  # 대기 차량이 있다면, 즉 주차 공간이 꽉 찼는데 들어온 차량이라면
            for i in range(n):  # 빈 공간을 찾아서 주차 공간 앞에서부터 탐색
                if parking_num > 0:  # 주차 공간이 남았고
                    if not parking[i]:  # 공간을 발견했다면
                        parking[i] = waiting.popleft()  # 대기 순서부터 주차
                        parking_num -= 1  # 공간 감소
                else:  # 주차 공간이 없다면 탐색할 필요 없으므로
                    break

        if car > 0:  # 입장 차량이라면
            if parking_num > 0:  # 남은 주차 공간이 있다면
                for i in range(n):  # 빈 공간을 찾아서 주차 공간 앞에서부터 탐색
                    if not parking[i]:  # 공간을 발견했다면
                        parking[i] = car  # 차량 주차
                        parking_num -= 1  # 공간 감소
                        break  # 더 이상 탐색할 필요가 없으니 종료
            else:  # 주차 공간이 없다면
                waiting.append(car)  # 다음 자리가 날 때 해당 차량이 먼저 들어가야하므로 일단 대기
        else:  # 출장 차량이라면
            car *= -1  # 차량 번호를 양수로 유지해야 하므로 -1 곱해줌

            for i in range(n):  # 해당 차량의 위치 탐색
                if parking[i] == car:  # 차량 발견
                    parking[i] = False  # 차량 출차
                    parking_num += 1  # 공간 증가
                    answer += w[car] * r[i]  # 차량의 무게 * 주창 공강별 단위 무게당 금액
                    break  # 더 이상 탐색할 필요가 없으니 종료

    print(f'#{t} {answer}')

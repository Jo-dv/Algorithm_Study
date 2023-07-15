n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
schedule.sort(key=lambda x: x[0])  # 시작 시간 기준 정렬
schedule.sort(key=lambda x: x[1])  # 종료 시간 기준 정렬
# x: (x[0], x[1])로 정렬할 경우 시작 시간이 같을 때만 종료 시간이 짧은 것을 우선 정렬함, 하지만 시작 시간과 종료 시간 모두 최소가 돼야 함 

answer = []  # 디버깅용, 정수를 저장하는 변수를 선언해서 증가시켜줘도 무방
end = 0  # 회의 종료 시간 초기화

for time in schedule:
    if time[0] >= end:  # 회의 시작 시간이 종료시간과 같거나 늦다면, 참고로 회의는 종료와 함께 시작될 수 있기 >=를 사용
        answer.append(time)  # 해당 회의 추가
        end = time[1]  # 마지막 회의 종료 시간 갱신

print(len(answer))

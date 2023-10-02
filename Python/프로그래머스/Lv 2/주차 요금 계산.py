from collections import deque
from math import ceil

def solution(fees, records):
    info = {}
    for i in records:
        temp = i.split()  # 차량들의 출차 정보 분리
        h, m = list(map(int, temp[0].split(':')))  # 시간을 시와 분으로 분리
        if temp[1] not in info.keys():  # 차량 번호가 등록되어 있지 않다면
            info[temp[1]] = deque([h * 60 + m])  # 해당 차량 번호와 함께 분으로 변환한 출차 시간을 저장
        else:
            info[temp[1]].append(h * 60 + m)  # 이미 있다면 시간만 저장

    for i in info.items():  # 저장된 정보들에 대해서, i[0]는 차량 번호, i[1]은 출차 시간
        if len(i[1]) % 2 != 0:  # 출차 기록이 짝수가 아니라면
            info[i[0]].append(23 * 60 + 59)  # 23:59분에 출차한 것으로 간주하여 그에 대한 정보 저장
        for j in range(len(i[1]) // 2):
            info[i[0]].appendleft(info[i[0]].pop() - info[i[0]].pop())  # 마지막 출차 정보부터 출차 - 입차 시간을 계선하여 저장
        total = sum(i[1])  # 해당 차량의 총 누적 출차 시간 계산
        info[i[0]] = fees[1] if total <= fees[0] else fees[1] + ceil((total - fees[0]) / fees[2]) * fees[3]
        # 누적 시간이 기본 시간 이하라면 해당 차량의 출차 정보를 기본 요금으로 초기화, 아니라면 조건에 맞춰 추가 계산된 요금으로 초기화

    return [i[1] for i in sorted(list(info.items()), key=lambda x: x[0])]  # 차량 번호를 오름차순으로 하여 요금만 추출

fees, records = [180, 5000, 10, 600], \
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
                "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
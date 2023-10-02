from collections import deque

progresses = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)  # 편의상 deque 자료형 사용
    speeds = deque(speeds)

    while progresses:
        task = 0
        for i in range(len(progresses)):  # 한 번 반복이 돌기 시작하면 남아있는 모든 작업에 대해 작업 진행
            progresses[i] += speeds[i]
        for _ in range(len(progresses)):  # 진행에 대한 반복이 완료되면 완료된 작업이 있느지 확인
            if progresses[0] >= 100:  # 작업이 완료되었을 경우
                progresses.popleft()  # deque 형태이므로 맨 앞의 데이터가 빠지면 그 다음 데이터가 자연스럽게 [0]의 위치가 된다.
                speeds.popleft()
                task += 1  # 처리된 작업량 증가
            else:  # 완료된 작업이 없다면
                break
        if task != 0:  # 처리된 작업량에 변동이 생겼을 경우에만
            answer.append(task)

    return answer

print(solution(progresses, speeds))
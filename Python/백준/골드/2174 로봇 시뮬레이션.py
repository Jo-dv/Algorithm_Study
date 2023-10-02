a, b = map(int, input().split())
n, m = map(int, input().split())
maps = [[0] * a for _ in range(b)]
direction = {'N': (-1, 0), 'W': (0, -1), 'S': (1, 0), 'E': (0, 1)}
nwse = list(direction.keys())  # 방향의 인덱스
robot_yx = []  # 로봇의 좌표를 저장할 리스트
robot_d = []  # 로봇의 방향을 저장할 리스트
flag = False  # 문제 발생 여부

for _ in range(n):
    x, y, d = input().split()  # 로봇의 위치와 방향을 입력받음
    robot_yx.append([b - int(y), int(x) - 1])  # 로봇의 위치 저장, 주의할 점은 y의 시작이 밑에서 아래임
    robot_d.append(d)
    maps[b - int(y)][int(x) - 1] = 1  # 로봇을 맵에 배치
cmds = [input().split() for _ in range(m)]  # 명령 입력

for mission in cmds:
    if not flag:  # 문제가 발생하지 않았다면
        n = int(mission[0]) - 1  # 로봇의 시작 번호는 1부터지만 인덱스 상 0번부터 저장되어 있으므로
        for _ in range(int(mission[2])):  # 명령 반복 횟수
            cy, cx = robot_yx[n]  # 현재 로봇의 위치
            i = nwse.index(robot_d[n])  # 현재 로봇의 방향

            if mission[1] == 'L':  # 정방향 0 1 2 3
                robot_d[n] = nwse[0] if i == 3 else nwse[i + 1]  # 왼쪽 회전 1 2 3 0
            elif mission[1] == 'R':
                robot_d[n] = nwse[3] if i == 0 else nwse[abs(i - 1)]  # 오른쪽 회전 3 0 1 2
            else:  # F 명령이라면
                my, mx = direction[robot_d[n]]  # 현재 방향 불러와서
                if not (0 <= cy + my < b and 0 <= cx + mx < a):  # 이동할 범위가 맵을 벗어났다면
                    print(f'Robot {mission[0]} crashes into the wall')  # 벽에 부딪힘
                    break  # 해당 명령 종료
                if maps[cy + my][cx + mx]:  # 이동할 위치에 다른 로봇이 있다면
                    robot_y = robot_yx.index([cy + my, cx + mx]) + 1  # 몇 번 로봇인지 찾아서, 역시 인덱스가 0부터 시작하므로 +1
                    print(f'Robot {mission[0]} crashes into robot {robot_y}')  # 로봇과 충돌
                    break  # 해당 명령 종료
                maps[cy][cx] = 0  # 벽과 로봇에 부딪히지 않았다면 이동
                maps[cy + my][cx + mx] = 1  # 이동할 위치에 로봇 배치
                robot_yx[n] = [cy + my, cx + mx]  # 해당 로봇의 위치(=배치) 정보 갱신
        else:  # break 없이 정상적으로 명령이 수행되었다면
            continue  # 다음 명령 확인
        flag = True  # 반복문이 제대로 종료되지 않았다는 의미로 플래그 갱신
    else:
        break  # 플래그가 갱신되었을 때, 더 이상 명령을 수행할 필요 없으므로 즉시 종료

if not flag:  # 명령 수행이 완전하게 종료되었을 때 실행, 해당 조건을 검사하지 않으면 사고 출력문과 함께 OK가 출력됨
    print('OK')  # 이상없음

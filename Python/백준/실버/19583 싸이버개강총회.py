import sys

input = lambda: sys.stdin.readline()


class Main:
    def __init__(self):
        self.s, self.e, self.q = input().split()
        self.log = dict()
        self.answer = 0

    def time_to_sec(self, time):  # 주어진 타임스탬프를 초단위로 변환
        h, m = time.split(":")
        return int(h) * 3600 + int(m) * 60

    def solve(self):
        self.s = self.time_to_sec(self.s)
        self.e = self.time_to_sec(self.e)
        self.q = self.time_to_sec(self.q)

        try:  # 몇 번의 입력이 들어올지 모르기 때문에 입력 에러가 나는 시점을 입력 종료시점으로 함
            while True:
                timestamp, name = input().split()
                time = self.time_to_sec(timestamp)
                if name not in self.log:  # 해당 유저의 기록이 없다면
                    if time <= self.s:  # 개강총회 전에 채팅을 쳤다면
                        self.log[name] = time  # 로그에 기록
                else:  # 기록이 있다면 개강총회 전에 채팅을 쳤다는 것을 의미
                    if self.e <= time <= self.q:  # 개강총회가 끝난 직후부터 스트리밍이 끝난 시점에 채팅을 쳤다면
                        self.log.pop(name)  # 해당 유저는 더 이상 체크할 필요 없음
                        self.answer += 1  # 확인된 인원 갱신
        except:
            print(self.answer)


problem = Main()
problem.solve()

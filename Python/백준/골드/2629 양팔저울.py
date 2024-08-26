class Main:
    def __init__(self):
        self.n = int(input())
        self.weights = list(map(int, input().split()))
        self.m = int(input())
        self.beads = list(map(int, input().split()))
        self.answer = []

    def solve(self):
        possible_weights = {0}  # 시작은 0 무게로 초기화

        for weight in self.weights:  # 가능한 무게 차이 계산 -> 계산된 무게 차이에 해당하는 무게의 구슬이 있다면 대칭 가능
            new_weights = set()
            for w in possible_weights:  # 현재 올릴 수 있는 무게들에 대해서
                new_weights.add(w + weight)  # 추를 한쪽에 올린 경우 -> 추의 조합 w에 현재 추를 추가
                new_weights.add(abs(w - weight))  # 추를 반대쪽에 올린 경우 -> 추의 조합 w 반대에 현재 추를 추가
            possible_weights.update(new_weights)  # 만들어진 조합을 추가

        for bead in self.beads:
            self.answer.append('Y' if bead in possible_weights else 'N')  # 만들어진 조합에 해당하는 구슬이 있는 경우

        print(' '.join(self.answer))


problem = Main()
problem.solve()
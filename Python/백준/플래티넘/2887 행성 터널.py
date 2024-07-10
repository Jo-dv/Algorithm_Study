import sys
input = lambda: sys.stdin.readline()  # 선언하지 않으면 테스트케이스에 따라 정답 혹은 시간 초과 발생

class Node:
    def __init__(self, index, x, y, z):
        self.index = index  # 노드 식별자
        self.x = x
        self.y = y
        self.z = z


class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost


class Main:
    def __init__(self):
        self.n = int(input())
        self.cord = [list(map(int, input().split())) for _ in range(self.n)]
        self.parents = [i for i in range(self.n)]
        self.answer = 0

    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        self.parents[y] = x
        return True

    @staticmethod  # Main 클래스의 인스턴스를 사용하지 않기 때문
    def cal_cost(p1, p2):
        return min(abs(p1.x - p2.x), abs(p1.y - p2.y), abs(p1.z - p2.z))

    def sort_and_add_edges(self, planet, edges, key):
        planet.sort(key=key)
        for i in range(self.n - 1):
            cost = Main.cal_cost(planet[i], planet[i + 1])
            edges.append(Edge(planet[i].index, planet[i + 1].index, cost))

    def solve(self):
        planet = [Node(i, x, y, z) for i, (x, y, z) in enumerate(self.cord)]
        edges = []

        # 각 좌표 별로 모든 노드 쌍을 고려하지 않고 N-1개의 터널을 만들 수 있는 최소의 노드만 선택
        self.sort_and_add_edges(planet, edges, key=lambda node: node.x)
        self.sort_and_add_edges(planet, edges, key=lambda node: node.y)
        self.sort_and_add_edges(planet, edges, key=lambda node: node.z)

        edges.sort(key=lambda edge: edge.cost)  # 최소 비용 계산을 위한 간선 정보 정렬

        tunnel = 0
        for e in edges:
            if self.union(e.start, e.end):  # MST를 이용해 노드들을 최소 비용을 가지는 그래프 생성
                if tunnel <= self.n - 1:
                    tunnel += 1
                    self.answer += e.cost
                else:
                    break

        print(self.answer)


problem = Main()
problem.solve()
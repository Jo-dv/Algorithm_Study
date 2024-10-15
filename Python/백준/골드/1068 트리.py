from collections import deque, defaultdict


class Tree:
    def __init__(self, n, parents, target):
        self.n = n
        self.target = target
        self.children = defaultdict(set)
        self.root = None

        # 트리 구축
        for child, parent in enumerate(parents):
            if parent == -1:
                self.root = child
            else:
                self.children[parent].add(child)

    def delete_node(self):
        dq = deque([self.target])
        while dq:
            node = dq.popleft()
            for child in self.children[node]:
                dq.append(child)
            del self.children[node]  # 노드 삭제

        # 부모의 자식 목록에서도 삭제할 노드 제거
        for parent, child_list in self.children.items():
            if self.target in child_list:
                self.children[parent].remove(self.target)

    def count_leaves(self):
        leaf_count = 0
        dq = deque([self.root])

        if self.root == self.target:
            return 0  # 루트를 삭제한 경우 남은 리프 노드는 0

        while dq:
            node = dq.popleft()
            if len(self.children[node]) == 0:
                leaf_count += 1
            else:
                for child in self.children[node]:
                    dq.append(child)

        return leaf_count


class Main:
    def __init__(self):
        self.n = int(input())
        self.parents = list(map(int, input().split()))
        self.target = int(input())

    def solve(self):
        tree = Tree(self.n, self.parents, self.target)
        tree.delete_node()
        result = tree.count_leaves()
        print(result)


problem = Main()
problem.solve()

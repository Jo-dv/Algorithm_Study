class Main:
    def __init__(self):
        self.doc = input()
        self.word = input()
        self.answer = 0

    def solve(self):
        idx = 0  # 문서 내에서 탐색을 시작할 위치

        while idx <= len(self.doc) - len(self.word):
            found = self.doc.find(self.word, idx)

            if found == -1:  # 단어가 더 이상 나타나지 않으면 종료
                break

            self.answer += 1
            idx = found + len(self.word)  # 겹치지 않게 단어의 마지막 위치 다음부터 다시 탐색 시작

        print(self.answer)


problem = Main()
problem.solve()
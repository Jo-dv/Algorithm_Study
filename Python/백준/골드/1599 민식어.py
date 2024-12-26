class Main:
    def __init__(self):
        self.n = int(input())
        self.words = [input() for _ in range(self.n)]
        self.answer = []

    def solve(self):
        alphabet = ['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']
        priority = [i for i in range(1, 21)]
        dic = dict((key, value) for key, value in zip(alphabet, priority))

        for word in self.words:
            data = []
            i = 0
            while i < len(word):
                if word[i:i+2] == "ng":
                    data.append(dic["ng"])
                    i += 2
                else:
                    data.append(dic[word[i]])
                    i += 1

            self.answer.append((data, word))

        for key, value in sorted(self.answer, key=lambda x: x[0]):
            print(value)


problem = Main()
problem.solve()

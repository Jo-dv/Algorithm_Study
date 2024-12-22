from collections import Counter


class Main:
    def __init__(self):
        self.name = list(input())
        self.answer = ""

    def solve(self):
        frequency = Counter(self.name)
        cnt = 0
        mid = ""

        for key, value in frequency.items():
            if value % 2 == 1:
                cnt += 1
                mid = key
                if cnt >= 2:
                    print("I'm Sorry Hansoo")
                    return

        result = ""
        for key, value in sorted(frequency.items()):
            result += (key * (value // 2))

        print(result + mid + result[::-1])


problem = Main()
problem.solve()
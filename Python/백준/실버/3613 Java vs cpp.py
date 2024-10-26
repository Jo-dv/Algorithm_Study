class Main:
    def __init__(self):
        self.var = input()
        self.answer = ""

    def solve(self):
        if self.var.count("_") == 0 and self.var[0].islower():  # Java to C++
            self.answer = ""
            cnt = 0
            for i in self.var:
                if i.isupper():
                    cnt += 1
            if cnt == 0:
                print(self.var)
                return
            else:
                for i in self.var:
                    if i.isupper():
                        self.answer += "_"
                    self.answer += i.lower()
                print(self.answer)
                return
        elif self.var.split("_").count("") == 0 and self.var.count("_") != 0 and self.var[0].islower() and self.var[-1].islower():  # C++ to Java
            self.answer = ""
            cnt = 0
            for i in self.var:
                if i.isalpha() and i.isupper():
                    cnt += 1
            if cnt == 0:
                for g_idx, group in enumerate(self.var.split("_")):
                    for c_idx, char in enumerate(group):
                        self.answer += char.upper() if c_idx == 0 and g_idx != 0 else char
                print(self.answer)
                return

        print("Error!")


problem = Main()
problem.solve()
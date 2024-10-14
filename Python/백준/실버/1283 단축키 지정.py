class Main:
    def __init__(self):
        self.n = int(input())
        self.options = [input() for _ in range(self.n)]
        self.answer = []

    def solve(self):
        used_shortcuts = set()

        for option in self.options:
            words = option.split()
            found_shortcut = False

            for idx, word in enumerate(words):
                first_letter = word[0].lower()
                if first_letter not in used_shortcuts:
                    modified_option = " ".join(words[:idx] + [f"[{word[0]}]{word[1:]}"] + words[idx + 1:])
                    self.answer.append(modified_option)
                    used_shortcuts.add(first_letter)
                    found_shortcut = True
                    break

            if not found_shortcut:
                for i, char in enumerate(option):
                    if char != ' ' and char.lower() not in used_shortcuts:
                        modified_option = option[:i] + f"[{char}]" + option[i + 1:]
                        self.answer.append(modified_option)
                        used_shortcuts.add(char.lower())
                        found_shortcut = True
                        break

            if not found_shortcut:
                self.answer.append(option)

        for i in self.answer:
            print(i)


problem = Main()
problem.solve()

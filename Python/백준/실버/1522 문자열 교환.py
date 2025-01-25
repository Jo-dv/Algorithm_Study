class Main:
    def __init__(self):
        self.string = input().strip()
        self.answer = float('inf')

    def solve(self):
        n = len(self.string)
        count_a = self.string.count('a')  # 'a'의 개수
        extended_string = self.string * 2  # 원형 문자열 처리

        # 슬라이딩 윈도우로 'b' 개수 계산
        current_b_count = extended_string[:count_a].count('b')  # 초기 윈도우
        self.answer = current_b_count

        for i in range(1, n):
            # 윈도우 이동: 이전 문자 제거, 다음 문자 추가
            if extended_string[i - 1] == 'b':
                current_b_count -= 1
            if extended_string[i + count_a - 1] == 'b':
                current_b_count += 1
            self.answer = min(self.answer, current_b_count)

        print(self.answer)


problem = Main()
problem.solve()

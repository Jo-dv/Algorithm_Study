from string import ascii_lowercase as lower

def dfs(i, word_set, count):
    global answer
    if i == n:  # 최대 n개 단어를 선택 가능하므로 n,
        if len(word_set) >= 26 and sorted(set(word_set)) == list(lower):
            # 모든 알파벳 26자 + 단어에 중복된 알파벳이 있을 수 있으므로 최소 26자리, 중복을 제거하고 정렬하여 알파벳 세트와 비교
            count += 1
        answer += count
        return  # 재귀 종료
    dfs(i + 1, word_set, count)  # 다음 단어로 넘어가서 해당 단어 선택하지 않음
    dfs(i + 1, word_set + word[i], count)  # 다음 단어로 넘어가서 해당 단어 선택


for t in range(1, int(input())+1):
    n = int(input())
    word = [input().rstrip() for _ in range(n)]  # 테스트 케이스에 개행 등의 공백이 마지막에 포함되나 봄, rstrip으로 제거
    answer = 0
    dfs(0, '', 0)  # word의 인덱스, 만들어진 단어 조합, 만들어진 단어 조합의 수

    print(f'#{t} {answer}')
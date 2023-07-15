n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

def solution(n, words):
    spoken_words = []
    count = [0] * n

    for i in range(len(words)):
        if words[i] not in spoken_words:
            if spoken_words and spoken_words[-1][-1] != words[i][0]:
                return [(i % n) + 1, count[i % n]+1]
            spoken_words.append(words[i])
            count[i % n] += 1
        else:
            return [(i % n) + 1, count[i % n]+1]

    return [0, 0]

print(solution(n, words))
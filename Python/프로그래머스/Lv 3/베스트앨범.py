from collections import defaultdict


def solution(genres, plays):
    answer = []
    album = defaultdict(list)
    total_play = defaultdict(int)

    for i, data in enumerate(zip(genres, plays)):
        k, v = data
        album[k].append((i, v))
        total_play[k] += v

    for i in album.values():
        i.sort(key=lambda x: (-x[1], x[0]))  # 장르 내에서 많이 재생된 노래, 고유 번호 낮은 순

    for k, v in total_play.items():
        album[k].append(v)

    result = sorted(list(album.items()), key=lambda x: -x[1][-1])

    for i in result:
        for j in range(min(2, len(i[1]) - 1)):
            answer.append(i[1][j][0])

    return answer

def solution(players, callings):
    idx = dict(zip(players, range(len(players))))  # 사람들의 이름과 현재 순위

    for i in callings:
        win_name, win_idx = i, idx[i] - 1  # 호명된 사람의 이름, 그 사람의 순위 상승
        lose_name, lose_idx = players[win_idx], idx[win_name]  # 호명된 사람의 앞 사람의 이름, 그 사람의 순위 하락(=이긴 사람의 원래 순위)
        players[win_idx], players[lose_idx] = win_name, lose_name  # 순서 스왑
        idx[win_name], idx[lose_name] = win_idx, lose_idx  # 현재 순위 정보 갱신

    return players

players, callings = ["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]

print(solution(players, callings))
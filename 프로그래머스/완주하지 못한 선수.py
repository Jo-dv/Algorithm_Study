from collections import Counter
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]

print(solution(participant, completion))
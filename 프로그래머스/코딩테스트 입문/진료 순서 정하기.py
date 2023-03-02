emergency = [3, 76, 24]

def solution(emergency):
    order = {i: j for i, j in zip(sorted(emergency, reverse=True), range(1, len(emergency)+1))}
    return [order[i] for i in emergency]

print(solution(emergency))
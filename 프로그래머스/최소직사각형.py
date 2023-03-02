sizes = [[60, 50],
         [30, 70],
         [60, 30],
         [80, 40]]

def solution(sizes):
    sizes = [sorted([j for j in i], reverse=True) for i in sizes]
    return max(list(zip(*sizes))[0]) * max(list(zip(*sizes))[1])

print(solution(sizes))

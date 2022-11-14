for t in range(1, int(input())+1):
    N = int(input())
    Ai, Bi = [], []
    same, diff, cross = 0, 0, 0

    for _ in range(N):
        A, B = map(int, input().split())
        Ai.append(A)
        Bi.append(B)
    A_max, A_min, B_max, B_min = max(Ai), min(Ai), max(Bi), min(Bi)

    if Ai.__eq__(Bi):
        print(f'#{t} {0}')
    else:
        for a, b in zip(Ai, Bi):
            if a == b:
                same += 1
            else:
                diff += 1
            if diff > 1 and a == A_min and b == B_max or diff > 1 and a == A_max and b == B_min:
                cross += 1
        print(f'#{t} {same * diff + cross}')
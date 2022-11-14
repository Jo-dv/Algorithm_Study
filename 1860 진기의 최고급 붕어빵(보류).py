for t in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    time = sorted(list(map(int, input().split())))
    flow = []
    count = 0

    for i, j in zip(range(N), time):
        flow.append([M, K])
        if j >= flow[i][0]:


    for i, j, k in zip(time[:-1], flow[:-1], range(N-1)):
        if i < j[0] or j[1] < 1:
            print(f'#{t} Impossible')
            break
        flow[k+1] -= 1
    else:
        print(f'#{t} Possible')

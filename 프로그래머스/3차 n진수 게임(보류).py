n = 16
t = 16
m = 2
p = 2

def solution(n, t, m, p):
    result = ''
    answer = ''
    for i in range(1, t*m+1):
        result += hex(i-1)[2:]
        if i % m == p:
            answer += result[i-1]
            print(hex(i-1)[2:])
    return answer.upper()

#print(solution(n, t, m, p)

for i in range(1, t*m+1):
    print(i % m, i % (m-1))
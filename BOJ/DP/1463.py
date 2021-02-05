n = int(input())
d = [0] * (n+1)
INF = 1000001

for i in range(2, n+1):
    result1 = d[i-1]
    if i % 2 == 0:
        result2 = d[i//2]
    else:
        result2 = INF
    if i % 3 == 0:
        result3 = d[i//3]
    else:
        result3 = INF

    d[i] = min(result1, result2, result3) + 1

print(d[n])

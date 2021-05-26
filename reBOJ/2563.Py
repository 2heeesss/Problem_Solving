n = int(input())
x, y = [0]*n, [0]*n
visted = [[0 for _ in range(101)] for _ in range(101)]
result = 0

for i in range(n):
    x[i], y[i] = map(int, input().split())
    for j in range(10):
        for k in range(10):
            visted[x[i]+j][y[i]+k] = 1

for n in range(101):
    result += sum(visted[n])

print(result)

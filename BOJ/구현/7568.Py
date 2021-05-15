n = int(input())
mans = []
result = [1]*n
for _ in range(n):
    mans.append(list(map(int, input().split())))


for i in range(n):
    for j in range(n):
        if (mans[i][0] < mans[j][0]) & (mans[i][1] < mans[j][1]):
            result[i] += 1

print(*result, sep=' ')

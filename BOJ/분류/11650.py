n = int(input())
xy = [0]*n

for i in range(n):
    xy[i] = list(map(int, input().split()))
xy.sort()

for i in range(n):
    print(xy[i][0], xy[i][1])

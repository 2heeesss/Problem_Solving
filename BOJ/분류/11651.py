n = int(input())
xy = [0]*n
temp = 0

for i in range(n):
    xy[i] = list(map(int, input().split()))

for j in range(n):
    temp = xy[j][0]
    xy[j][0] = xy[j][1]
    xy[j][1] = temp
xy.sort()
for j in range(n):
    temp = xy[j][0]
    xy[j][0] = xy[j][1]
    xy[j][1] = temp


for k in range(n):
    print(xy[k][0], xy[k][1])

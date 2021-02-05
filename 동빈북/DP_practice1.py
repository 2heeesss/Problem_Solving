n = int(input())
box = list(map(int, input().split()))

d = [0]*n

d[0] = box[0]
d[1] = max(box[0], box[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+box[i])

print(d[n-1])

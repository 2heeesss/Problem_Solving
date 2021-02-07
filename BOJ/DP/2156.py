import sys
read = sys.stdin.readline
n = int(read())
arr = [0]
for j in range(n):
    arr.append(int(read()))
d = [0]

d.append(arr[1])
if n > 1:
    d.append(arr[1]+arr[2])

for i in range(3, n+1):
    d.append(max(d[i-1], d[i-2] + arr[i], d[i-3] + arr[i] + arr[i-1]))

print(d[n])

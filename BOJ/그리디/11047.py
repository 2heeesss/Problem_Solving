n, k = map(int, input().split())
arr = [0]*n
count = 0
d = 0
for i in range(n):
    arr[i] = int(input())

for j in range(n):
    d = k // arr[n-j-1]
    k = k - d * arr[n-j-1]
    count = count + d
    if k == 0:
        break
print(count)

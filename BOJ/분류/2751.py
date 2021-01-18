n = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())

arr.sort()

for j in range(n):
    print(arr[j])

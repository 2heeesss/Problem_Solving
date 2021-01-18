n = int(input())
arr = list(map(int, input().split()))
sum_arr = [0]*n

del arr[n:1000]
arr.sort()

count = 0
for i in range(n):
    for j in range(i+1):
        count = count + arr[j]
print(count)

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
sum = 0
for i in range(m):
    if (k) % (i+1) == 0:
        sum += arr[1]
        print('if')
    else:
        sum += arr[0]
        print('else')
print(sum)

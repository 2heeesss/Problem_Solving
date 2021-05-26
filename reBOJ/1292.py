a, b = map(int, input().split())
arr = []
result = 0

for i in range(100):
    for j in range(i):
        arr.append(i)

for i in range(a-1, b):
    result += arr[i]

print(result)

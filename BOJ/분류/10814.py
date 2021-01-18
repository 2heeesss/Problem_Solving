n = int(input())
arr = [0]*n


for i in range(n):
    arr[i] = list(input().split())

arr.sort()

print(arr.index('Junkyu'))

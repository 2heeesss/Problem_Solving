import sys
input = sys.stdin.readline

t = int(input().rstrip())
arr = [0]*t

for i in range(t):
    arr[i] = list(map(int, input().rstrip().split()))
    arr[i].sort(reverse=True)
    print(arr[i][2])

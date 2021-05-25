import sys

input = sys.stdin.readline
T = int(input().rstrip())
arr = [input().rstrip().split() for _ in range(T)]
for i in range(T):
    for j in range(len(arr[i][1])):
        for _ in range(int(arr[i][0])):
            print(arr[i][1][j], end='')
    print()

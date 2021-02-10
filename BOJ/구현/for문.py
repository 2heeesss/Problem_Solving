# import sys
# read = sys.stdin.readline
# t = int(read().rstrip())
# arr = [0]*t
# result = [0]*t
# for i in range(t):
#     arr[i] = list(map(int, read().split()))
#     result[i] = arr[i][0]+arr[i][1]

# for j in range(t):
#     print(result[j])


# 10871 - x보다 작은 수
import sys
read = sys.stdin.readline

n, x = map(int, read().split())
arr = list(map(int, read().split()))
for number in arr:
    if number < x:
        print(number, end=' ')

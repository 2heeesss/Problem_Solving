import sys
input = sys.stdin.readline
n = int(input())
arr = {}

for _ in range(n):
    name, state = input().split()
    if state == 'enter':
        arr[name] = 1
    else:
        arr[name] = 0

arr = sorted(arr.items(), key=lambda x: x[1])
arr = sorted(arr, reverse=True)

for i in arr:
    if i[1] > 0:
        print(i[0])

# 스텍에 집어넣어서 append, remove 를 사용 -> 실패~
# remove 는 O(n)시간을 잡아먹음

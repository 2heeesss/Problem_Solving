# 입력 많이 받아야 할 경우 sys.stdin.readline()으로 받아주자!
# 이진탐색 함수 안에서 인덱스 사용 까먹지 말기

import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
arrCheck = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0

arr.sort()


def bin(arr, start, end, target):
    if start > end:
        return None
    mid = (start+end)//2
    if target == arr[mid]:
        return 1
    elif target < arr[mid]:
        return bin(arr, start, mid-1, target)
    else:
        return bin(arr, mid+1, end, target)


for i in arrCheck:
    result = bin(arr, 0, n-1, i)
    if result != None:
        print(result)
    else:
        print(0)

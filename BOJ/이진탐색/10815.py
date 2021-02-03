import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
arrCheck = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()


def binary_check(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if target == arr[mid]:
        return 1
    elif target < arr[mid]:
        return binary_check(arr, target, start, mid-1)
    else:
        return binary_check(arr, target, mid+1, end)


for i in arrCheck:
    result = 0
    result = binary_check(arr, i, 0, n-1)
    if result != None:
        print(1, end=' ')
    else:
        print(0, end=' ')

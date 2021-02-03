n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(arr)


def binary(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        end = mid - 1
        return binary(arr, target, start, end)
    elif target > arr[mid]:
        start = mid + 1
        return binary(arr, target, start, end)


result = binary(arr, target, 0, n-1)

print(result + 1)

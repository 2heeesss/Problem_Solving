n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
currentTape = 0
print(arr)
for hole in arr:
    if currentTape > hole:
        pass
    else:
        cnt += 1
        currentTape = hole + l - 0.5

print(cnt)

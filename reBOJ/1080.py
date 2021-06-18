n, m = map(int, input().split())
arr1 = [list(map(int, input())) for _ in range(n)]
wantArr = [list(map(int, input())) for _ in range(n)]
cnt = 0
result = True


def changeMap(x, y, arr):
    for i in range(x, x+3):
        for j in range(y, y+3):
            arr[i][j] = 1 - arr[i][j]
    return arr


for i in range(n-2):
    for j in range(m-2):
        if arr1[i][j] != wantArr[i][j]:
            arr1 = changeMap(i, j, arr1)
            cnt += 1

for i in range(n):
    for j in range(m):
        if arr1[i][j] != wantArr[i][j]:
            result = False

if result:
    print(cnt)
else:
    print(-1)


# range(10)은 0부터 10까지가 아니라, 10번 반복

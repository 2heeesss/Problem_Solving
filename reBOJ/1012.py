import sys
from collections import deque


input = sys.stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([[x, y]])
    arr[x][y] = 0
    while queue:
        v = queue.popleft()
        vx, vy = v[0], v[1]
        for i in range(4):
            xx = vx + dx[i]
            yy = vy + dy[i]
            if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 1:
                arr[xx][yy] = 0
                queue.append([xx, yy])


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)

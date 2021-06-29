from collections import deque
import sys


def bfs(x, y):
    queue = deque([[x, y]])
    graph[x][y] = 0
    while queue:
        v = queue.popleft()
        for i in range(8):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])


while True:
    input = sys.stdin.readline
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)

# if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
# 순서 다를때 조건도 달라짐

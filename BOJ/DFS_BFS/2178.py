from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visted = [[0]*m for _ in range(n)]


def bfs():
    queue = [(0, 0)]
    visted[0][0] = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visted[nx][ny] == 0 and graph[nx][ny] == 1:
                    visted[nx][ny] = visted[x][y] + 1
                    queue.append((nx, ny))


bfs()
print(visted[n-1][m-1])

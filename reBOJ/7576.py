from collections import deque


def bfs(arr):
    queue = deque(arr)
    while queue:
        v = queue.popleft()
        for i in range(4):
            nx = v[0]+dx[i]
            ny = v[1]+dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] += graph[v[0]][v[1]] + 1
                queue.append([nx, ny])


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
arr = []
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            arr.append([i, j])

bfs(arr)

for i in range(len(graph)):
    if 0 in graph[i]:
        result = -1
        break
    if result < max(graph[i])-1:
        result = max(graph[i])-1
print(result)

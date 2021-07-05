import sys
from collections import deque
input = sys.stdin.readline


def bfs(x):
    visted[x] = True
    queue = deque([x])
    while queue:
        v = queue.popleft()
        for i in range(len(graph[v])):
            if not visted[i] and graph[v][i] == 1:
                visted[i] = True
                queue.append(i)


n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for k in range(n):
    graph[k+1][k+1] = 1
visted = [False]*(n+1)
cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(n+1):
    for j in range(n+1):
        if not visted[j] and graph[i][j] == 1:
            bfs(j)
            cnt += 1
print(cnt)

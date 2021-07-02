import sys
from collections import deque
input = sys.stdin.readline


def bfs(i):
    queue = deque([i])
    while queue:
        v = queue.popleft()
        for k in range(len(graph[v])):
            if graph[v][k] == 1 and visted[k] == 0:
                visted[k] = visted[v] + 1
                graph[v][k] = 0
                queue.append(k)


n = int(input())
x, y = map(int, input().split())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
visted = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

bfs(x)
if visted[y] == 0:
    print(-1)
else:
    print(visted[y])

from collections import deque


def dfs(v):
    visted[v] = True
    print(v, end=' ')
    for i in range(len(graph[v])):
        if visted[i] == False and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    visted = [False]*(n+1)
    queue = deque([v])
    visted[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(len(graph[v])):
            if not visted[i] and graph[v][i] == 1:
                queue.append(i)
                visted[i] = True


n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
visted = [False]*(n+1)
dfs(v)
print()
bfs(v)

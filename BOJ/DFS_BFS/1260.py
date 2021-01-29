from collections import deque


def dfs(graph, v, visted):
    visted[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visted[i]:
            visted[i] = True
            dfs(graph, i, visted)


def bfs(graph, start, visted):
    queue = deque([start])
    visted[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visted[i]:
                queue.append(i)
                visted[i] = True


n, m, v = map(int, input().split())

graph = [[0 for j in range(0)] for i in range(n+1)]
for i in range(m):
    edge_front, edge_back = map(int, input().split())
    graph[edge_front].append(edge_back)
    graph[edge_back].append(edge_front)
# 그래프 정렬하기
for node in graph:
    node.sort()


visted_dfs = [False]*(n+1)
visted_bfs = [False]*(n+1)

dfs(graph, v, visted_dfs)
print()
bfs(graph, v, visted_bfs)

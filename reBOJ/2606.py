from collections import deque


def bfs(v):
    visted[v] = True
    queue = deque([v])
    cnt = 0
    while queue:
        x = queue.popleft()
        for node in graph[x]:
            if not visted[node]:
                visted[node] = True
                queue.append(node)
                cnt += 1
    return cnt


n = int(input())
m = int(input())
visted = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))


# graph = [[0]*(n+1)]
# graph = [[0] for _ in range(n+1)]

from collections import deque
# BFS 는 큐 자료구조 사용. 기본적으로 append, popleft로 구현함


def BFS(graph, start, visted):
    queue = deque([start])  # 큐에 시작노드 저장
    visted[start] = True    # 시작노드 방문처리

    while queue:            # 큐가 없어질때까지
        v = queue.popleft()  # 먼저 들어간 노드 없애기
        print(v, end=' ')

        for i in graph[v]:  # 먼저 들어간 노드의 인접노드 탐색
            if not visted[i]:  # 방문하지 않았으면
                queue.append(i)  # 큐에 저장
                visted[v] = True  # 방문처리


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visted = [False]*9
BFS(graph, 1, visted)

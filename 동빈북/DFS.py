def DFS(graph, start, visted):
    # 시작노드 방문처리
    visted[start] = True
    print(start, end='')
    # 인접노드 방문시작
    for node in graph[start]:
        if visted[node] == False:   # not visted[node] 로 하는게 더 좋은거야
            DFS(graph, node, visted)


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


DFS(graph, 1, visted)

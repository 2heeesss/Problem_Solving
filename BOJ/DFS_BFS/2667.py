n = int(input())
a = [list(map(int, input())) for _ in range(n)]
# 방향벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
ans = []
# 방문처리 위해
dist = [[False] * n for _ in range(n)]


def dfs(x, y):
    global cnt
    # 몇평짜리 인지 카운트 증가, 방문처리
    cnt += 1
    dist[x][y] = True
    # 4방향 전부 탐색
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 범위 안에서
        if 0 <= nx < n and 0 <= ny < n:
            # 집이있고, 방문하지않았으면 dfs 수행
            if a[nx][ny] == 1 and dist[nx][ny] == False:
                dfs(nx, ny)


# 행렬 0,0 부터 하나씩 탐색
for i in range(n):
    for j in range(n):
        # 만약 집이 있고, 방문하지 않았으면 dfs 수행
        if a[i][j] == 1 and dist[i][j] == False:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

print(len(ans))
ans.sort()
print('\n'.join(map(str, ans)))

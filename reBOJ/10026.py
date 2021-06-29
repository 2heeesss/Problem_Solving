from collections import deque


def bfs(x, y, normalFlag):
    color = graph[x][y]
    queue = deque([[x, y]])
    if normalFlag:  # 정상인
        vistedNormal[x][y] = True
    else:  # 적록색맹
        vistedBlind[x][y] = True
        if color == 'R' or color == 'G':
            colorFlag = True
        else:
            colorFlag = False

    while queue:
        v = queue.popleft()
        for i in range(4):
            nx = v[0]+dx[i]
            ny = v[1]+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if normalFlag:  # 정상인 케이스
                    # 방문하지 않음 + 색 같음
                    if not vistedNormal[nx][ny] and graph[nx][ny] == color:
                        queue.append([nx, ny])
                        vistedNormal[nx][ny] = True
                elif not normalFlag:  # 적록색맹 케이스
                    if not vistedBlind[nx][ny]:
                        # 방문하지 않음 + 색 == R,G or 색 == B
                        if colorFlag and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G'):
                            queue.append([nx, ny])
                            vistedBlind[nx][ny] = True
                        if not colorFlag and (graph[nx][ny] == 'B'):
                            queue.append([nx, ny])
                            vistedBlind[nx][ny] = True


n = int(input())
graph = [list(input()) for _ in range(n)]
vistedNormal = [[False]*n for _ in range(n)]
vistedBlind = [[False]*n for _ in range(n)]
cntNormal, cntBlind = 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(n):
        if not vistedNormal[i][j]:
            bfs(i, j, True)
            cntNormal += 1
        if not vistedBlind[i][j]:
            bfs(i, j, False)
            cntBlind += 1

print(cntNormal, cntBlind)


# 두가지방법
# 리스트는 하나만 만들고 함수로 두가지경우 쳐내기
# 리스트 두개 만들고 함수 하나로쓰기

# if color == 'R' or color == 'G':

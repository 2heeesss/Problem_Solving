import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]
result = 0


def ch(x, y):
    cntW = 0
    cntB = 0
    for i in range(x, x+8):
        for j in range(y, y+1):
            if i % 2 == 0:
                cntW += int(graph[i][j+0] == 'W') + int(graph[i][j+1] == 'B') + \
                    int(graph[i][j+2] == 'W') + int(graph[i][j+3] == 'B') + \
                    int(graph[i][j+4] == 'W') + int(graph[i][j+5] == 'B') + \
                    int(graph[i][j+6] == 'W') + int(graph[i][j+7] == 'B')

                cntB += int(graph[i][j+0] == 'B') + int(graph[i][j+1] == 'W') +\
                    int(graph[i][j+2] == 'B') + int(graph[i][j+3] == 'W') + \
                    int(graph[i][j+4] == 'B') + int(graph[i][j+5] == 'W') + \
                    int(graph[i][j+6] == 'B') + int(graph[i][j+7] == 'W')
            else:
                cntW += int(graph[i][j+0] == 'B') + int(graph[i][j+1] == 'W') +\
                    int(graph[i][j+2] == 'B') + int(graph[i][j+3] == 'W') + \
                    int(graph[i][j+4] == 'B') + int(graph[i][j+5] == 'W') + \
                    int(graph[i][j+6] == 'B') + int(graph[i][j+7] == 'W')

                cntB += int(graph[i][j+0] == 'W') + int(graph[i][j+1] == 'B') + \
                    int(graph[i][j+2] == 'W') + int(graph[i][j+3] == 'B') + \
                    int(graph[i][j+4] == 'W') + int(graph[i][j+5] == 'B') + \
                    int(graph[i][j+6] == 'W') + int(graph[i][j+7] == 'B')
    return max(cntW, cntB)


for i in range(n-7):
    for j in range(m-7):
        result = max(ch(i, j), result)

print(64-result)

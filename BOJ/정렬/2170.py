import sys

n = int(sys.stdin.readline())
line = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
# x1 정렬
line.sort()
# line 리스트의 시작, 끝값 저장
startPoint = line[0][0]
endPoint = line[0][1]

for i in range(1, len(line)):
    if startPoint <= line[i][0] <= endPoint:
        if endPoint < line[i][1]:
            endPoint = line[i][1]
        else:
            continue
    else:
        cnt += line[i][1] - line[i][0]

endPoint = int(endPoint)
startPoint = int(startPoint)
print(endPoint-startPoint+cnt)

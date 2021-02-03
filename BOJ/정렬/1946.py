import sys

t = int(sys.stdin.readline())
cnt = [1] * t
for i in range(t):
    n = int(sys.stdin.readline())
    # score = [[0] for _ in range(n)]
    score = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    score.sort()
    minScore = score[0][1]

    for j in range(1, len(score)):
        if minScore > score[j][1]:
            minScore = score[j][1]
            cnt[i] += 1

for i in cnt:
    print(i)

import sys
from collections import deque

input = sys.stdin.readline
c = int(input().rstrip())
while c != 0:
    scores = deque(map(int, input().rstrip().split()))
    n = scores.popleft()
    average = sum(scores) / n

    result = 0
    for score in scores:
        if score > average:
            result += 1
    print(format(result/n*100, "0.3f"), '%', sep='')

    c -= 1

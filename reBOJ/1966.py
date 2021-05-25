import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, target = map(int, input().rstrip().split())
    imp = deque(map(int, input().rstrip().split()))
    idx = deque(range(len(imp)))
    idx[target] = 'Target'
    order = 0

    while True:
        if imp[0] == max(imp):
            order += 1
            if idx[0] == 'Target':
                print(order)
                break
            else:
                imp.popleft()
                idx.popleft()
        else:
            imp.append(imp.popleft())
            idx.append(idx.popleft())

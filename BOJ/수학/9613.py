import sys
from math import gcd
from collections import deque

read = sys.stdin.readline

for _ in range(int(read())):
    arr = deque(map(int, read().split()))
    k = arr.popleft()
    result = 0

    for i in range(k):
        for j in range(k):
            if i < j:
                result += gcd(arr[i], arr[j])

    print(result)

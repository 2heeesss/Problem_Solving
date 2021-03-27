import sys
from collections import Counter

input = sys.stdin.readline
nums = []
for _ in range(10):
    nums.append(int(input().rstrip()) % 42)

print(len(Counter(nums)))

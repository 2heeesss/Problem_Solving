import sys
input = sys.stdin.readline

nums = []
k = int(input().rstrip())
for _ in range(k):
    num = int(input().rstrip())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)
print(sum(nums))

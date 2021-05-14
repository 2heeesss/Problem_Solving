n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()

print(*nums, sep='\n')

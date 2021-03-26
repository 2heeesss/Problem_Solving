import sys
input = sys.stdin.readline

nums = []
for i in range(9):
    nums.append([int(input().rstrip()), i+1])
nums.sort(reverse=True)

print(nums[0][0], nums[0][1], sep='\n')

import sys
input = sys.stdin.readline
n = int(input().rstrip())

rope = []
result = []
for i in range(n):
    rope.append(int(input().rstrip()))
rope.sort(reverse=True)

for i in range(n):
    result.append(rope[i]*(i+1))

print(max(result))

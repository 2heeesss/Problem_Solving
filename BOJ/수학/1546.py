import sys
input = sys.stdin.readline

n = int(input().rstrip())
scores = list(map(int, input().rstrip().split()))
m = max(scores)
result = 0

for score in scores:
    result += score / m * 100

result = result / len(scores)
print(result)

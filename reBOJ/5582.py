import sys
input = sys.stdin.readline
w1 = input().rstrip()
w2 = input().rstrip()

dp = [[0]*(len(w2)+1) for _ in range(len(w1)+1)]
result = 0

for i in range(1, len(w1)+1):
    for j in range(1, len(w2)+1):
        if w1[i-1] == w2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            result = max(result, dp[i][j])
print(result)

# l = min(len(w1)-i, len(w2)-j)
# for k in range(1, l):
#     if w1[i+k] == w2[j+k]:
#         cnt += 1
#     else:
#         break
# result.append(cnt)
# cnt = 0

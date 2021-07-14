import sys
input = sys.stdin.readline

w1 = input().rstrip()
w2 = input().rstrip()
lenOfw1 = len(w1)
lenOfw2 = len(w2)
dp = [[0]*(lenOfw2+2) for _ in range(lenOfw1+2)]
result = 0

for i in range(2, lenOfw1+2):
    for j in range(2, lenOfw2+2):
        dp[i-1][j-1] = max(dp[i-2][j-2], dp[i-1][j-2],
                           dp[i-2][j-1], dp[i-1][j-1])
        if w1[i-2] == w2[j-2]:
            dp[i][j] = dp[i-1][j-1] + 1
            result = max(dp[i][j], result)
print(result)

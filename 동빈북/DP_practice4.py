t = int(input())
result = [0]*t
for i in range(t):

    n, m = map(int, input().split())  # list 없어도 됨
    arr = list(map(int, input().split()))
    dp = []
    index = 0
    for _ in range(n):
        dp.append(arr[index:index + m])  # 인덱스 슬라이싱
        index += m

    for j in range(1, m):
        for k in range(n):
            if k == 0:
                left_up = 0
            else:
                left_up = dp[k-1][j-1]
            if k == n-1:
                left_down = 0
            else:
                left_down = dp[k+1][j-1]
            left = dp[k][j-1]
            dp[i][j] = max(left_up, left_down, left)+dp[i][j]

    result = 0
    for j in range(n):
        result = max(result, dp[j][m-1])
    print(result)

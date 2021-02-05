n, m = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append(int(input()))

d = [10001]*(m+1)
d[0] = 0
for coin in arr:  # 모든 화폐 순회
    for j in range(coin, m+1):  # 2원부터 시작, m+1(입력 값)원까지
        if d[j - coin] != 10001:
            d[j] = min(d[j], d[j - coin]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

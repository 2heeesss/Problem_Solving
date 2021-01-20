# 3
T = int(input())
arr = [0]*T
address = [0]*T

for i in range(T):
    arr[i] = list(map(int, input().split()))

for i in range(T):
    h = arr[i][0]
    w = arr[i][1]
    n = arr[i][2]
    if n % h == 0:
        height = (10**2)*(h)
        width = n//h
    else:
        height = (10**2)*(n % h)
        width = n//h + 1
    address[i] = height+width

for i in range(T):
    print(address[i])

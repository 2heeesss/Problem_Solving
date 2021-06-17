a, b = map(int, input().split())
cnt = 0
while True:
    if b % 2 == 0:
        b //= 2
        cnt += 1
    elif b % 10 == 1:
        b = str(b)
        b = int(b[0:-1])
        cnt += 1
    else:
        print(-1)
        break

    if b == a:
        print(cnt+1)
        break
    elif b < a:
        print(-1)
        break

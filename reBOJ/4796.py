i = 1
arr = []
while True:
    l, p, v = list(map(int, input().split()))
    if l+p+v == 0:
        break
    result = (v//p) * l
    if (v % p) < l:
        result += v % p
    else:
        result += l
    arr.append("Case "+str(i)+": "+str(result))
    i += 1
for i in arr:
    print(i)

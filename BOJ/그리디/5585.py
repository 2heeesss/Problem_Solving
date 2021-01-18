n = int(input())
k = 1000 - n
count = 0
while True:
    if k >= 500:
        k -= 500
        count += 1
    elif k >= 100:
        k -= 100
        count += 1
    elif k >= 50:
        k -= 50
        count += 1
    elif k >= 10:
        k -= 10
        count += 1
    elif k >= 5:
        k -= 5
        count += 1
    elif k >= 1:
        k -= 1
        count += 1

    if k == 0:
        break

print(count)

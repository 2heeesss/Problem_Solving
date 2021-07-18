a, b = map(int, input().split(':'))

maxNum, minNum = max(a, b), min(a, b)
k = 1
while True:
    if maxNum % minNum == 0:
        k = minNum
        break
    maxNum, minNum = minNum, maxNum % minNum

print(a//k, end=':')
print(b//k)

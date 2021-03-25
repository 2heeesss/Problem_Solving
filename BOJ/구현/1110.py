import sys
input = sys.stdin.readline

n = int(input().rstrip())
if n < 10:
    n *= 10

count = 0
newNum = 99999
tens, unit = n//10, n % 10


while newNum != n:
    addNum = tens + unit
    newNum = (unit)*10 + addNum % 10
    tens, unit = newNum//10, newNum % 10
    count += 1

print(count)

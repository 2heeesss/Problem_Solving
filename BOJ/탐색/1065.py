import sys


def isHanNum(one, ten, hun):
    first = ten - one
    second = hun - ten
    if first == second:
        return 1
    return 0


def d(number):
    if 1 <= number <= 99:
        return 1
    elif 100 <= number <= 999:
        ones = number % 10
        tens = (number // 10) % 10
        huns = (number // 10) // 10
        return isHanNum(ones, tens, huns)
    else:
        return 0


input = sys.stdin.readline
n = int(input().rstrip())
cnt = 0
result = []

while n != cnt:
    result.append(d(cnt+1))
    cnt += 1

print(sum(result))

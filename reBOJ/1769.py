import sys
input = sys.stdin.readline
s = input().rstrip()
cnt = 0


def sumStr(str):
    result = 0
    for num in str:
        result += int(num)
    return result


def isLessTen(str):
    if len(str) < 2:
        return True
    return False


while True:
    if isLessTen(s):
        print(cnt)
        if int(s) % 3 == 0:
            print('YES')
            break
        print('NO')
        break
    else:
        cnt += 1
    s = str(sumStr(s))

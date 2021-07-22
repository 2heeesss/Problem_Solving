import sys
input = sys.stdin.readline
s = list(map(int, input().rstrip()))

cnt0, cnt1 = 0, 0
stk = []

for i in s:
    if not stk or stk[-1] != i:
        stk.append(i)
        if i == 0:
            cnt0 += 1
        else:
            cnt1 += 1

if cnt1 >= cnt0:
    print(cnt0)
else:
    print(cnt1)

# count 사용법

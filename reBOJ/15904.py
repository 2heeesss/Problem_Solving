import sys
input = sys.stdin.readline

word = input().rstrip()
stk = []
flag = False

for i in word:
    if not stk:
        if i == 'U':
            stk.append(i)
    else:
        if stk[-1] == 'U' and i == 'C':
            stk.append(i)
        if stk[-1] == 'C' and i == 'P':
            stk.append(i)
        if stk[-1] == 'P' and i == 'C':
            stk.append(i)
            flag = True
            break

if flag:
    print('I love UCPC')
else:
    print('I hate UCPC')

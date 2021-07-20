import sys
input = sys.stdin.readline

word = input().rstrip()
bomb = input().rstrip()
stk = []
lw, lb = len(word), len(bomb)

for i in word:
    stk.append(i)
    if len(stk) >= lb and ('').join(stk[-lb:]) == bomb:
        for _ in range(lb):
            stk.pop()

if stk:
    print(('').join(stk))
else:
    print('FRULA')

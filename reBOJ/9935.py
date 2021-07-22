import sys
input = sys.stdin.readline

word = input().rstrip()
bomb = input().rstrip()
lastChar = bomb[-1]
stk = []
lw, lb = len(word), len(bomb)

for i in word:
    stk.append(i)
    if i == lastChar and ('').join(stk[-lb:]) == bomb:
        for _ in range(lb):
            stk.pop()

if stk:
    print(('').join(stk))
else:
    print('FRULA')

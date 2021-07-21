import sys
input = sys.stdin.readline
word = input().rstrip()
check = input().rstrip()
stk = []
cnt = 0
checkLength = len(check)
for i in word:
    stk.append(i)
    if ('').join(stk[-checkLength:]) == check:
        cnt += 1
        stk.clear()
print(cnt)

# pop 말고 clear 해줌

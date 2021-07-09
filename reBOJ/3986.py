import sys
input = sys.stdin.readline

cnt = 0
for _ in range(int(input())):
    arr = input().rstrip()
    stack = [arr[0]]
    for i in range(1, len(arr)):
        if not stack:
            stack.append(arr[i])
        else:
            if arr[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(arr[i])
    if len(stack) == 0:
        cnt += 1

print(cnt)

import sys
input = sys.stdin.readline


arr = []
while True:
    words = list(input().rstrip())
    if words[0] == '.':
        break
    arr.append(words)
result = ['yes'] * len(arr)

for i in range(len(arr)):
    stack = []
    for word in arr[i]:
        if word == '(' or word == '[':
            stack.append(word)
        elif word == ')' or word == ']':
            if len(stack) == 0:
                result[i] = 'no'
                break
            if word == ')':
                if stack[-1] == '[':
                    result[i] = 'no'
                    break
            if word == ']':
                if stack[-1] == '(':
                    result[i] = 'no'
                    break
            stack.pop()
    if len(stack) >= 1:
        result[i] = 'no'

    print(result[i])

# ((()) 이거 생각 못하고 stack에 문자가 남아있을경우 생각못함
# 간단한건데 반례를 생각못함 흠..

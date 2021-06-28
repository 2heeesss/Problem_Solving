from collections import deque

t = int(input())
arr = [deque(input()) for _ in range(t)]
for i in range(t):
    result = []
    for j in range(len(arr[i])):
        word = arr[i].popleft()
        if word == '(':
            result.append('(')
        else:
            if len(result) == 0 or (j == 0 and word == ')'):
                result.append(True)
                break
            result.pop()
    if len(result) == 0:
        print('YES')
    else:
        print('NO')


# 첫번째 시도
# t = int(input())
# arr = [list(input()) for _ in range(t)]
# result = [0] * t
# for i in range(t):
#     leftParenthesis, rightParenthesis = 0, 0
#     while arr[i]:
#         word = arr[i].pop()
#         if word == '(':
#             leftParenthesis += 1
#         else:
#             rightParenthesis += 1

#     if leftParenthesis == rightParenthesis:
#         result[i] = 'YES'
#     else:
#         result[i] = 'NO'

# print(result)

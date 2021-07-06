from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    originalPwd = list(input().rstrip())
    left, right = [], deque([])
    for alphabet in originalPwd:
        if alphabet == '<':
            if left:
                right.appendleft(left.pop())
        elif alphabet == '>':
            if right:
                left.append(right.popleft())
        elif alphabet == '-':
            if left:
                left.pop()
        else:
            left.append(alphabet)
    left.extend(right)
    print(''.join(left))

# import sys
# input = sys.stdin.readline

# for _ in range(int(input().rstrip())):
#     originalPwd = list(input().rstrip())
#     left, right = [], []
#     for alphabet in originalPwd:
#         if alphabet == '<':
#             if left:
#                 right.append(left.pop())
#         elif alphabet == '>':
#             if right:
#                 left.append(right.pop())
#         elif alphabet == '-':
#             if left:
#                 left.pop()
#         else:
#             left.append(alphabet)
#     left.extend(reversed(right))
#     print(''.join(left))

# 시도1 시간초과

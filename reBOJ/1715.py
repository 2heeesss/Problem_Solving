import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
cnt = 0
heapq.heapify(cards)

while True:
    if n == 1:
        print(0)
        break
    if len(cards) == 2:
        print(sum(cards)+cnt)
        break

    v1 = heapq.heappop(cards)
    v2 = heapq.heappop(cards)
    heapq.heappush(cards, v1+v2)
    cnt += v1+v2

# while True:
#     if n == 1:
#         print(0)
#         break
#     if n == 2:
#         print(sum(cards))
#         break
#     if flag:
#         cards.sort()
#         for i in range(len(cards)//2):
#             stack.append(cards[i*2]+cards[(i*2)+1])
#             cnt += cards[i*2]+cards[(i*2)+1]
#         if len(cards) % 2 == 1:
#             stack.append(cards[-1])
#         if len(stack) == 2:
#             print(sum(stack)+cnt)
#             break
#         cards.clear()
#     else:
#         stack.sort()
#         for i in range(len(stack)//2):
#             cards.append(stack[i*2]+stack[(i*2)+1])
#             cnt += stack[i*2]+stack[(i*2)+1]
#         if len(stack) % 2 == 1:
#             cards.append(stack[-1])
#         if len(cards) == 2:
#             print(sum(cards)+cnt)
#             break
#         stack.clear()
#     flag = not flag

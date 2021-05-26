n, k = map(int, input().split())
arr = [False for _ in range(n+1)]
cnt = 0
breakPoint = False

for i in range(2, n+2):
    for j in range(i, n+1, i):
        if arr[j] == False:
            arr[j] = True
            cnt += 1
        if cnt == k:
            print(j)
            breakPoint = True
            break
    if breakPoint == True:
        break

        # from collections import deque

        # n, k = map(int, input().split())
        # arr = [i for i in range(2, n)]
        # arr = deque(arr)
        # visted = [False for _ in range(n+1)]
        # visted[0], visted[1] = True, True
        # cnt = 0
        # while cnt != k:
        #     if n == 2 or len(arr) < 1:
        #         p = 2
        #     else:
        #         p = arr.popleft()

        #     for i in range(n):
        #         if p*i >= len(visted):
        #             break

        #         if visted[p*i] == False:
        #             visted[p*i] = True
        #             cnt += 1
        #             if cnt == k:
        #                 print(p*i)
        #                 break

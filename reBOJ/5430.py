import sys
from collections import deque
input = sys.stdin.readline


for _ in range(int(input())):
    func = input().rstrip()
    l = int(input())
    arr = input().rstrip()
    if l > 0:
        nums = deque(list(map(int, arr[1:-1].split(','))))
    else:
        nums = []
    leftPop = True
    result = True

    for i in func:
        if i == 'R' and leftPop:
            leftPop = False
        elif i == 'R' and not leftPop:
            leftPop = True
        elif i == 'D' and leftPop:
            if not nums:
                result = False
                break
            nums.popleft()
        elif i == 'D' and not leftPop:
            if not nums:
                result = False
                break
            nums.pop()

    if result:
        numsFinal = list(nums)
        if leftPop:
            print('['+','.join(map(str, numsFinal))+']')
        else:
            print('['+','.join(map(str, numsFinal[::-1]))+']')
    else:
        print('error')


# list.count('문자') 사용방법 처음씀
# 1차시도 ValueError
# 배열로 들어오는 숫자가 2자리수 이상이면 잘 안됨
# 리스트 뒤집는법
# 리스트 슬라이싱 [1:-1]

# def newList(array, length):
#     n = []
#     i = 1
#     for _ in range(length):
#         n.append(int(array[i]))
#         i += 2
#     return n

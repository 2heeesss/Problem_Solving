import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
numberList = []
numberList = Counter(map(int, sys.stdin.readline().split()))


m = int(sys.stdin.readline().rstrip())
numberCheckList = []
numberCheckList = list(map(int, sys.stdin.readline().split()))


for number in numberCheckList:
    if number in numberList:
        print(numberList[number], end=' ')
    else:
        print(0, end=' ')

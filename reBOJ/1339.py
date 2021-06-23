# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(list(input().rstrip()))

# wordArr = [0]*10
# wordSize = 9
# result = 0

# while True:
#     maxLength, maxIndex = 0, 0

#     for i in range(len(arr)):
#         if len(arr[i]) > maxLength:
#             maxLength = len(arr[i])
#             maxIndex = i
#         elif len(arr[i]) == maxLength:
#             a, b = 0, 0
#             if len(arr[maxIndex]) == 0:
#                 break
#             for p in range(len(arr)):
#                 a += arr[p].count(arr[maxIndex][0])
#                 b += arr[p].count(arr[i][0])
#             if a > b:
#                 continue
#             else:
#                 maxIndex = len(arr[i])
#                 maxIndex = i

#     if len(arr[maxIndex]) == 0:
#         break
#     else:
#         alphabet = arr[maxIndex].pop(0)

#     if alphabet in wordArr:
#         for j in range(len(wordArr)):
#             if alphabet == wordArr[j]:
#                 result += j*(10**(maxLength-1))
#     else:
#         wordArr[wordSize] = alphabet
#         result += wordSize*(10**(maxLength-1))
#         wordSize -= 1

# print(result)


import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input().rstrip()))
wordDict = {}

for word in arr:
    k = len(word)-1
    for alphabet in word:
        if alphabet in wordDict:
            wordDict[alphabet] += 10 ** k
        else:
            wordDict[alphabet] = 10 ** k
        k -= 1

print(wordDict)
sortWords = sorted(wordDict.values(), reverse=True)
p = 9
result = 0
for word in sortWords:
    print(word)
    result += word*p
    p -= 1

print(result)
# 딕셔너리 사용법
# 딕셔너리 정렬방법

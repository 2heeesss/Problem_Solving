# for in range와 리스트 넣었을때 차이점
import sys
from collections import Counter
n = int(sys.stdin.readline().rstrip())
numberList = [0]*n
for i in range(n):
    numberList[i] = int(sys.stdin.readline().rstrip())
    # numberList.append(int(sys.stdin.readline()))

numberList.sort()


def average(numbers, n):
    return round(sum(numbers)/n)
    # 반올림


def middle(numbers, n):
    if n % 2 == 0:
        return (numbers[n//2] + numbers[n//2 + 1])/2
    else:
        return numbers[n//2]


def frequency(numbers, n):
    nums_s = Counter(numberList).most_common()  # 새로 알게된 사실
    if len(nums_s) > 1:
        if nums_s[0][1] == nums_s[1][1]:
            return nums_s[1][0]
        else:
            return nums_s[0][0]
    else:
        return nums_s[0][0]

    # ******* 내가 썼었던 방법 *******
    # if n == 1:
    #     return numbers[0]

    # fre = [[0]*2 for _ in range(n)]
    # for j in range(n):
    #     fre[j][1] = numbers[j]
    #     for k in range(j+1, n):
    #         if numbers[j] == numbers[k]:
    #             fre[j][0] += 1

    # fre.sort(reverse=True)
    # newList = [4001]*n
    # for k in range(n):
    #     if fre[0][0] == fre[k][0]:
    #         newList[k] = fre[k][1]
    # newList.sort()
    # return newList[1]


def rangee(numbers, n):
    if n == 1:
        return 0
    return numbers[n-1] - numbers[0]


print(average(numberList, n))
print(middle(numberList, n))
print(frequency(numberList, n))
print(rangee(numberList, n))

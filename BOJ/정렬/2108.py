# for in range와 리스트 넣었을때 차이점
import sys
n = int(sys.stdin.readline().rstrip())
numberList = [0]*n
for i in range(n):
    numberList[i] = int(sys.stdin.readline().rstrip())

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
    if n == 1:
        return numbers[0]

    fre = [[0]*2 for _ in range(n)]
    for j in range(n):
        fre[j][1] = numbers[j]
        for k in range(j+1, n):
            if numbers[j] == numbers[k]:
                fre[j][0] += 1

    print(fre)

    min = fre[0][0]
    result = fre[0][1]
    # if min == 0:
    #     fre.sort()
    fre.sort(reverse=True)
    print(fre)

    for m in range(1, n):
        if min == 0:
            return result

        if min != fre[m][0]:
            return result
        # elif min == fre[m][0]:
        #     min = fre[m][0]
        #     result = fre[m][1]


def rangee(numbers, n):
    if n == 1:
        return 0
    return numbers[n-1] - numbers[0]


print(average(numberList, n))
print(middle(numberList, n))
print(frequency(numberList, n))
print(rangee(numberList, n))

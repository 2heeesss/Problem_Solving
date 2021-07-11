import sys
input = sys.stdin.readline


def isPalin(word):
    mid = len(word)//2
    result = 0
    for i in range(mid):
        if not word[i] == word[-(i+1)]:
            if isLeftPseudoPalin(i, mid, word) or isRightPseudoPalin(i, mid, word):
                return 1
            else:
                return 2
    return 0


def isRightPseudoPalin(i, mid, word):
    for j in range(i, mid):
        if not word[j] == word[-(j+2)]:
            return False
    return True


def isLeftPseudoPalin(i, mid, word):
    for j in range(i, mid):
        if not word[j+1] == word[-(j+1)]:
            return False
    return True


for _ in range(int(input())):
    v = input().rstrip()
    print(isPalin(v))


# 30분째 유사회문을 검색하는 로직이 잘 생각이 안남 회문인지 아닌지는 통과함

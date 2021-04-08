import sys


def checkGroupWord(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        else:
            for j in range(i+1, len(word)):
                if word[i] == word[j]:
                    return 0
    return 1


input = sys.stdin.readline
n = int(input().rstrip())
cnt = 0

while n != 0:
    word = input().rstrip()
    cnt += checkGroupWord(word)
    n -= 1

print(cnt)

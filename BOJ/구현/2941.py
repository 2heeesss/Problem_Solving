import sys
input = sys.stdin.readline
croAlphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = list(input().rstrip())
word.append('*')
cnt = 0

for i in range(len(word)-2):
    if word[i]+word[i+1] in croAlphabet:
        cnt += 1
        word[i+1] = '*'
    if word[i]+word[i+1]+word[i+2] in croAlphabet:
        cnt += 2
        word[i+1] = '*'
        word[i+2] = '*'
print(len(word)-1-cnt)

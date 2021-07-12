word = input().rstrip()
words = {}
result = [0 for _ in range(len(word))]
cnt = 0

# 입력받은 문자를 딕셔너리 자료형 words 에 저장
for alphabet in word:
    if alphabet in words.keys():
        words[alphabet] += 1
    else:
        words[alphabet] = 1
# 문자를 기준으로 정렬
sortedWords = sorted(words.items(), key=lambda x: x[0])

# words 딕셔너리에 홀수번 들어온 문자가 있으면 카운트 증가, 인덱스 저장
for k in range(len(sortedWords)):
    if not sortedWords[k][1] % 2 == 0:
        cnt += 1
        oddWord = sortedWords[k][0]
        sortedWords[k] = list(sortedWords[k])
        sortedWords[k][1] -= 1

# 홀수번 들어온 문자가 2개 이상이면 한수 못함
if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    c = 0
    for i in range(len(sortedWords)):
        for _ in range(sortedWords[i][1]//2):
            result[c], result[-c-1] = sortedWords[i][0], sortedWords[i][0]
            c += 1
    if cnt == 1:
        result[(len(word)//2)] = oddWord
    print(''.join(map(str, result)))

# print(''.join(result)) 이거때문에 틀린지 몰랐음..

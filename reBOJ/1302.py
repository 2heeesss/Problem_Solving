import sys
input = sys.stdin.readline
bookTuple = {}
result = []
for _ in range(int(input())):
    book = input().rstrip()
    if book in bookTuple:
        bookTuple[book] += 1
    else:
        bookTuple[book] = 1

books = sorted(bookTuple.items(), key=lambda x: x[1], reverse=True)
max = books[0][1]
for num in books:
    if num[1] == max:
        result.append(num[0])
    else:
        break
result.sort()
print(result[0])

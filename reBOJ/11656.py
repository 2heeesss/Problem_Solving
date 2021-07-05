a = input()
arr = [a[i:] for i in range(len(a))]
arr.sort()
for word in arr:
    print(word)

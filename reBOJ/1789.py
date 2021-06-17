s = int(input())
arr = []

for i in range(s):
    arr.append(i)
    if s-sum(arr) in arr:
        print(len(arr)-1)  # 0부터 담으니까
        break

word = input()
n = int(input())
arr = [input() for _ in range(n)]
for i in range(len(arr)):
    arr[i] += arr[i][0]+arr[i][1]+arr[i][2]+arr[i][3]+arr[i][4] + \
        arr[i][5]+arr[i][6]+arr[i][7]+arr[i][8]+arr[i][9]
cnt = 0
for i in range(len(arr)):
    if word in arr[i]:
        cnt += 1
print(cnt)

# 접근1 리스트로 확인하면서 -> 이건 너무오래걸릴듯
# 접근2 문자열로 확인

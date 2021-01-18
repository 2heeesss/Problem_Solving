n = list(map(int, input()))
set_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
check_list = [0]*10
double_num = 0

for i in n:
    for j in range(10):
        if i == set_list[j]:
            check_list[j] += 1


double_num = check_list[6]+check_list[9]

if double_num % 2 == 0:
    double_num = int(double_num/2)
else:
    double_num = double_num//2 + 1

check_list[6], check_list[9] = 0, 0
check_list[6] = double_num

print(max(check_list))

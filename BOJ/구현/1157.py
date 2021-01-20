input_word = list(input())

# 사전자료형으로 묶어서 풀라했는데 잘 안돼서 그냥 리스트로 풀기..
alphabet_list = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0,
    'K': 0,
    'L': 0,
    'M': 0,
    'N': 0,
    'O': 0,
    'P': 0,
    'Q': 0,
    'R': 0,
    'S': 0,
    'T': 0,
    'U': 0,
    'V': 0,
    'W': 0,
    'X': 0,
    'Y': 0,
    'Z': 0,
}
key_list = list(alphabet_list.keys())
value_list = list(alphabet_list.values())
# 입력받은 값들 대문자로 바꿔주기(대문자로 출력해야하니까)
uppercase = [x.upper() for x in input_word]  # 그냥 upper 하니까 안되더라 다시 확인해보세용

# 입력받은 단어 알파벳 별로 카운팅
for word in uppercase:
    for j in range(len(key_list)):
        if word == key_list[j]:
            value_list[j] += 1

# 가장 많이 사용된 알파벳 1개 이상인지 확인
max_value = max(value_list)
max_count = 0
for i in range(len(value_list)):
    if value_list[i] == max_value:
        max_count += 1

# max 알파벳이 1개 초과하면 ?, 1개면 그거 출력
# 2
if max_count > 1:
    print('?')
else:
    max_index = value_list.index(max(value_list))
    print(key_list[max_index])

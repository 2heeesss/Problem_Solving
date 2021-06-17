arr = list(input())

alphabet = [[], [], [],
            ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'],
            ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'],
            ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
result = 0

for alpha in arr:
    for i in range(len(alphabet)):
        if alpha in alphabet[i]:
            result += i

print(result)

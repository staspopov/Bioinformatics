
pattern = input()

result = ""

for i in range(len(pattern)-1, -1, -1):
    if pattern[i] == 'G':
        result += 'C'
    elif pattern[i] == 'C':
        result += 'G'
    elif pattern[i] == 'A':
        result += 'T'
    elif pattern[i] == 'T':
        result += 'A'

print(result)
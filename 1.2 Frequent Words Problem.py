genome = input()
k = int(input())

result = []
max_value = -1

for i in range(0, len(genome) - k + 1):

    current = genome[i: i + k]
    value = 1

    for j in range(i + 1, len(genome) - k + 1):
        if genome[j: j + k] == current:
            value += 1;

    if value == max_value:
        result.append(current)
    if value > max_value:
        max_value = value
        result = [current]

for i in result:
    print(i," ")

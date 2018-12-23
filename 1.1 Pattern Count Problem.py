pattern = input()
genome = input()
count = 0

for i in range(len(genome) - len(pattern)):
    if pattern == genome[i:i + len(pattern)]:
        count += 1


print(count)

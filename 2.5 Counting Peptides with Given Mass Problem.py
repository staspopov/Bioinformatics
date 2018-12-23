m = int(input())

masses = (57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186)

mass = [0 for i in range(0, m + 1)]
mass[0] = 1

for i in range(0, m + 1):
    for j in range(0, len(masses)):
        mass[i] += mass[i - masses[j]]

print(mass[m])
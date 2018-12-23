mass = {
    'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129,
    'Q' : 128, 'G' : 57, 'H' : 137, 'I' : 113, 'L' : 113, 'K' : 128,
    'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186,
    'Y' : 163, 'V' : 99
}

def get_mass(amino_acid_peptide):
    summ = 0
    for i in amino_acid_peptide:
        summ += mass.get(i)
    return summ

amino_acid_peptide = input()

cyclospectrum = [0]
size = len(amino_acid_peptide)

for i in range(1, size):
    for j in range(1, size + 1):
        if j - i < 0:
            cyclospectrum.append(get_mass(amino_acid_peptide[j - i:] + amino_acid_peptide[: j]))
        else:
            cyclospectrum.append(get_mass(amino_acid_peptide[j - i: j]))

cyclospectrum.append(get_mass(amino_acid_peptide))
cyclospectrum.sort()

for i in cyclospectrum:
    print(i)
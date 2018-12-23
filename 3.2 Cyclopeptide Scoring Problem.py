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

def cyclospectrum(peptide):

    cyclospectrum = [0]
    size = len(peptide)

    for i in range(1, size):
        for j in range(1, size + 1):
            if j - i < 0:
                cyclospectrum.append(get_mass(peptide[j - i:] + peptide[: j]))
            else:
                cyclospectrum.append(get_mass(peptide[j - i: j]))

    cyclospectrum.append(get_mass(peptide))
    cyclospectrum.sort()

    return cyclospectrum

def scoring(peptide, spectrum):
    p_spect = cyclospectrum(peptide)
    spect_copy = spectrum.copy()
    score = 0

    for i in p_spect:
        if i in spect_copy:
            spect_copy.remove(i)
            score +=1

    return score

peptide = input()

spectrum = [int(i) for i in input().split()]

print (scoring(peptide, spectrum))
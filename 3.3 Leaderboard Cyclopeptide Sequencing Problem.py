import sys

masses = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103,
    'I': 113, 'N': 114, 'D': 115, 'K': 128, 'E': 129, 'M': 131,
    'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
}

def mass(peptide):
    return sum([masses[s] for s in peptide])


def expand(peptides):
    new_peptides = []
    for peptide in peptides:
        for p in masses:
            new_peptides.append(peptide + p)
    return new_peptides


def linear_spect(peptide):
    if len(peptide) == 1:
        return str(masses[peptide])

    out_masses = [0]

    m = 0
    for s in peptide:
        out_masses.append(masses[s])
        m += masses[s]
    out_masses.append(m)

    for i in range(2, len(peptide)):
        for j in range(0, len(peptide) - i):
            subpeptide = peptide[j:j + i]
            cur_mass = 0
            for s in subpeptide:
                cur_mass += masses[s]
            out_masses.append(cur_mass)

    return " ".join(str(x) for x in sorted(out_masses))


def scoring(peptide, spectrum):
    peptide_masses = linear_spect(peptide).split(' ')
    spectrum_masses = spectrum.split(' ')
    score_value = 0
    for cmass in peptide_masses:
        if cmass in spectrum_masses:
            spectrum_masses.remove(cmass)
            score_value += 1

    return score_value


def trim(leaderboard, spectrum, n):
    leaderboard = sorted(leaderboard, key=lambda peptide: scoring(peptide, spectrum), reverse=True)
    if len(leaderboard) > n:
        last = n
        for i in range(n, len(leaderboard)):
            if scoring(leaderboard[n-1], spectrum) == scoring(leaderboard[i], spectrum):
                last = i
            else:
                break
        leaderboard = leaderboard[:last+1]
    return leaderboard


def main():
    n = int(sys.stdin.readline().rstrip())
    spectrum = sys.stdin.readline().rstrip()
    parent_mass = int(spectrum.split(' ')[-1])

    leaderboard = [""]
    leader_peptide = ""

    while len(leaderboard) > 0:
        while len(leaderboard) > 0:
            leaderboard = expand(leaderboard)
            immutable_peptides = leaderboard[:]
            for peptide in immutable_peptides:
                if mass(peptide) == parent_mass:
                    if scoring(peptide, spectrum) > scoring(leader_peptide, spectrum):
                        leader_peptide = peptide
                elif mass(peptide) > parent_mass:
                    leaderboard.remove(peptide)
            leaderboard = trim(leaderboard, spectrum, n)

    output_masses = []
    for s in leader_peptide:
        output_masses.append(masses[s])
    print("-".join([str(m) for m in output_masses]))


if __name__ == '__main__':
    main()
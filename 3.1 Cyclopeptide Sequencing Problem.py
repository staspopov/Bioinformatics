import sys

masses = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103,
    'I': 113, 'N': 114, 'D': 115, 'K': 128, 'E': 129, 'M': 131,
    'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
}


def get_mass(peptide):
    m = 0
    for s in peptide:
        m += masses[s]
    return m


def expand(peptides):
    new_peptides = []
    for peptide in peptides:
        for p in masses:
            new_peptides.append(peptide + p)
    return new_peptides


def cyclospectrum(peptide):
    out_masses = [0]

    m = 0
    for s in peptide:
        out_masses.append(masses[s])
        m += masses[s]
    out_masses.append(m)

    cycle_peptide = peptide + peptide

    for i in range(2, len(peptide)):
        for j in range(0, len(peptide)):
            subpeptide = cycle_peptide[j:j + i]
            cur_mass = 0
            for s in subpeptide:
                cur_mass += masses[s]
            out_masses.append(cur_mass)

    return " ".join(str(x) for x in sorted(out_masses))


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


def is_consistent(peptide, spectrum):
    spec_mass = [int(x) for x in spectrum.split(' ')]
    peptide_mass = [int(x) for x in linear_spect(peptide).split(' ')]
    for m in peptide_mass:
        if m in spec_mass:
            pass
        else:
            return False
    return True


def main():
    spectrum = sys.stdin.readline().rstrip()
    parent_mass = int(spectrum.split(' ')[-1])

    peptides = [""]
    output_peptides = []

    while len(peptides) > 0:
        peptides = expand(peptides)
        immutable_peptides = peptides[:]
        for peptide in immutable_peptides:
            if get_mass(peptide) == parent_mass:
                if cyclospectrum(peptide).strip() == spectrum.strip():
                    output_peptides.append(peptide)
                peptides.remove(peptide)
            elif not is_consistent(peptide, spectrum):
                peptides.remove(peptide)

    output_masses = []
    for p in output_peptides:
        m = []
        for s in p:
            m.append(masses[s])
        output_masses.append('-'.join([str(x) for x in m]))
    print(" ".join(output_masses))


if __name__ == '__main__':
    main()
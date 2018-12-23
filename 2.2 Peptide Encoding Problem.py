RNA_dict = {
    'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T',
    'ACU': 'T', 'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I',
    'AUG': 'M', 'AUU': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H', 'CCA': 'P',
    'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E',
    'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A', 'GGA': 'G', 'GGC': 'G',
    'GGG': 'G', 'GGU': 'G', 'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 'UAA': '',
    'UAC': 'Y', 'UAG': '', 'UAU': 'Y', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
    'UGA': '', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C', 'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'
}

def dna_to_rna(dna):
    rna = ""
    for i in dna:
        if i == 'T':
            rna += 'U'
        else:
            rna += i
    return rna


def protein_trnslt(rna_pattern):
    peptide = ""
    i = 0

    while i < len(rna_pattern):

        current = rna_pattern[i: i + 3]

        if RNA_dict.get(current) == None:
            i += 1
        else:
            peptide += RNA_dict.get(current)
            i += 3

    return (peptide)

def rna_reverse(rna):
    result = ""

    for i in range(len(rna) - 1, -1, -1):
        if rna[i] == 'G':
            result += 'C'
        elif rna[i] == 'C':
            result += 'G'
        elif rna[i] == 'A':
            result += 'U'
        elif rna[i] == 'U':
            result += 'A'

    return (result)

def main ():
    dna = input()
    amino_acid_peptide = input()

    result = []
    current_size = len(amino_acid_peptide) * 3
    rna = dna_to_rna(dna)

    for i in range(len(dna) - current_size + 1):
        if protein_trnslt(rna[i: i + current_size]) == amino_acid_peptide:
            result.append(dna[i: i + current_size])
        if protein_trnslt(rna_reverse(rna[i: i + current_size])) == amino_acid_peptide:
            result.append(dna[i: i + current_size])

    for i in result:
        print(i)

if __name__ == "__main__":
    main()
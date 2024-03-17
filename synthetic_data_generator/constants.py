import enum

aa_to_codon_table = {
    "F": [
        "TTT",
        "TTC"
    ],
    "L": [
        "TTA",
        "TTG",
        "CTT",
        "CTC",
        "CTA",
        "CTG"
    ],
    "I": [
        "ATT",
        "ATC",
        "ATA"
    ],
    "M": [
        "ATG"
    ],
    "V": [
        "GTT",
        "GTC",
        "GTA",
        "GTG"
    ],
    "S": [
        "TCT",
        "TCC",
        "TCA",
        "TCG",
        "AGT",
        "AGC"
    ],
    "P": [
        "CCT",
        "CCC",
        "CCA",
        "CCG"
    ],
    "T": [
        "ACT",
        "ACC",
        "ACA",
        "ACG"
    ],
    "A": [
        "GCT",
        "GCC",
        "GCA",
        "GCG"
    ],
    "Y": [
        "TAT",
        "TAC"
    ],
    "*": [
        "TAA",
        "TAG",
        "TGA"
    ],
    "H": [
        "CAT",
        "CAC"
    ],
    "Q": [
        "CAA",
        "CAG"
    ],
    "N": [
        "AAT",
        "AAC"
    ],
    "K": [
        "AAA",
        "AAG"
    ],
    "D": [
        "GAT",
        "GAC"
    ],
    "E": [
        "GAA",
        "GAG"
    ],
    "C": [
        "TGT",
        "TGC"
    ],
    "W": [
        "TGG"
    ],
    "R": [
        "CGT",
        "CGC",
        "CGA",
        "CGG",
        "AGA",
        "AGG"
    ],
    "G": [
        "GGT",
        "GGC",
        "GGA",
        "GGG"
    ]
}

codon_to_aa_table = {"TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
                     "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M", "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
                     "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                     "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T", "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                     "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*", "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                     "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K", "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                     "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W", "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                     "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

nucleotide_list = ["A", "T", "C", "G"]


class Nucleotide(enum.Enum):
    A = "A"
    T = "T"
    C = "C"
    G = "G"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

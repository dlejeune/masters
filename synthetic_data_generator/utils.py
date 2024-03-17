import random
import constants


def gen_seq(length):
    return "".join(random.choices(list(constants.codon_to_aa_table.keys()), k=length))


def introduce_gap(seq, gap_size, gap_start):
    return seq[:gap_start] + seq[gap_start + gap_size:]


def introduce_insertion(seq, insertion_start, insertion=None, insertion_size=10):
    if insertion is None:
        insertion = gen_seq(insertion_size)
    return seq[:insertion_start] + insertion + seq[insertion_start:]


def introduce_errors(seq, error_rate=0.01):
    return "".join([base if random.random() > error_rate else random.choice(constants.nucleotide_list) for base in seq])


def amplify_seq(seq, num_copies):
    seqs = []
    for i in range(num_copies):
        seqs.append(seq)

    return seqs


def dict_to_fasta(seq_dict, filename):
    with open(filename, "w") as f:
        for name, seq in seq_dict.items():
            f.write(f">{name}\n{seq}\n")

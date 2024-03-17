import utils
import random
import random_name_generator
import numpy as np
import typer


def main():
    random.seed(42)
    base_seq = utils.gen_seq(10)

    total_seqs = 10

    seqs = utils.amplify_seq(base_seq, total_seqs)

    deletion_prop = 0.1
    insertion_prop = 0.1
    frameshift_prop = 0.1

    seqs_with_deletion = int(total_seqs * deletion_prop)
    seqs_with_insertion = int(total_seqs * insertion_prop)
    seqs_with_frameshift = int(total_seqs * frameshift_prop)

    possible_insertion_sites = [0, 5, 15]
    possible_deletion_sites = [0, 5, 15, 22]

    average_gap_size = 10
    max_num_indels = 1

    output_seqs = {}

    output_seqs["ref"] = base_seq

    for _ in range(int(seqs_with_deletion)):
        new_seq = utils.introduce_gap(base_seq, average_gap_size, random.choice(possible_deletion_sites))
        new_name = random_name_generator.get_random_name(exclude=output_seqs)
        output_seqs[new_name] = new_seq

    for _ in range(int(seqs_with_insertion)):
        new_seq = utils.introduce_insertion(base_seq, random.choice(possible_deletion_sites),
                                            insertion_size=average_gap_size)
        new_name = random_name_generator.get_random_name(exclude=output_seqs)

        output_seqs[new_name] = new_seq

    seqs = utils.amplify_seq(base_seq, total_seqs - seqs_with_deletion - seqs_with_insertion)

    for seq in seqs:
        seq_name = random_name_generator.get_random_name(exclude=output_seqs)
        output_seqs[seq_name] = seq

    utils.dict_to_fasta(output_seqs, "output.fasta")


if __name__ == "__main__":
    typer.run(main)

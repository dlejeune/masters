import subprocess
import typer

def run_muscle(input_fasta: str, output_fasta: str):
    process = subprocess.run(f"muscle5.1 -align {input_fasta} -output {output_fasta}_muscle.fasta", shell=True)


def run_mafft(input_fasta: str, output_fasta: str):
    process = subprocess.run(f"mafft {input_fasta} > {output_fasta}_mafft.fasta", shell=True)

def main():
    input_file = "output.fasta"
    output_file = "aligned"
    run_muscle(input_file, output_file)
    run_mafft(input_file, output_file)
    pass


if __name__ == "__main__":
    typer.run(main)
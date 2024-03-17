# Synthetic FASTA generator

Okay, just brainstorming. We want to generate multiple copies of the same sequence. 

We will also want to add gaps, indels, or mutations. We should specify these somehow.

Maybe we can make a class that describes how to make these mutations:

- `x`% of reads should have gaps from pos `a` to `b`
- `y`% of reads should have 
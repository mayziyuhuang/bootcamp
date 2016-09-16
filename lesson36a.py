# practice 1
import pytest
import numpy as np

def find_codon_lesson6(codon, seq):
    """Find a specified codon with a given sequence."""

    i = 0
    count = 0
    # Scan sequence until we hit the start codon or the end of the sequence
    for i in range(0, len(seq), 3):
        while seq[i:i+3] != codon and i < len(seq):
            count += 1


        if i == len(seq):
            return -1
            break
        

    return count

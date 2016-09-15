# py.test gives the testing functionality
import pytest

# We'll use our bioinformatics dictionary from before
import bioinfo_dicts as bd

def n_neg(seq):
    """number of negative residues in a protein sequence"""

    # convert sequence to upper case
    seq = seq.upper()

    # check for a valid sequence
    for aa in seq:
        if aa not in bd.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')

    # count E and D and retrun the count
    return seq.count('E') + seq.count('D')

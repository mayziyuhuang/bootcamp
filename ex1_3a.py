def complement_base(base, material = 'DNA'):
    """Returns the Watson-Crick complement of a base."""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

def reverse_complement_norev(seq, material = 'DNA'):
    """Compute reverse complement of a sequence."""

    # Initialize reverse complement
    rev_comp = ''
    revseq = seq[::-1]

    for base in revseq:
        rev_comp += complement_base(base, material = material)

    return rev_comp

#exercise solution
#def reverse_complement(seq):
#    """Compute reverse complement of a sequence."""

    # Initialize reverse complement
#    rev_seq = ''

    # Loop through and populate list with reverse complement
#    for base in seq:
#        rev_seq += complement_base(base)

#    return rev_seq[::-1]

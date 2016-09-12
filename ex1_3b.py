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

def reverse_complement_nofor(seq, material = 'DNA'):
    """Compute reverse complement of a sequence."""

    # Initialize reverse complement
    rev_comp = ''
    revseq = seq[::-1]

    if material == 'DNA':
        rev_comp = revseq.replace('T', 'a')
        rev_comp = rev_comp.replace('A', 't')
        rev_comp = rev_comp.replace('C', 'g')
        rev_comp = rev_comp.replace('G', 'c')

        rev_comp = rev_comp.replace('a', 'A')
        rev_comp = rev_comp.replace('t', 'T')
        rev_comp = rev_comp.replace('g', 'G')
        rev_comp = rev_comp.replace('c', 'C')
    else:
        rev_comp = revseq.replace('U', 'a')
        rev_comp = rev_comp.replace('A', 'u')
        rev_comp = rev_comp.replace('C', 'g')
        rev_comp = rev_comp.replace('G', 'c')

        rev_comp = rev_comp.replace('a', 'A')
        rev_comp = rev_comp.replace('u', 'U')
        rev_comp = rev_comp.replace('g', 'G')
        rev_comp = rev_comp.replace('c', 'C')


    return rev_comp

#exercise solution
#def reverse_complement(seq):
#    """Compute reverse complement of a sequence."""

    # Initialize rev_seq to a lowercase seq
#    rev_seq = seq.lower()

    # Substitute bases
#    rev_seq = rev_seq.replace('t', 'A')
#    rev_seq = rev_seq.replace('a', 'T')
#    rev_seq = rev_seq.replace('g', 'C')
#    rev_seq = rev_seq.replace('c', 'G')

#    return rev_seq[::-1]

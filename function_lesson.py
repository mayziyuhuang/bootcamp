def ratio(x, y):
    """ The ratio of 'x' to 'y'. """
    return x / y

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

def reverse_complement(seq, material = 'DNA'):
    """Compute reverse complement of a sequence."""

    # Initialize reverse complement
    rev_comp = ''

    for base in reversed(seq):
        rev_comp += complement_base(base, material = material)

    return rev_comp


def answer_to_the_ultimate_question_of_life_the_universe_and_everything():
    """Simpler program than Deep THought's, I bet. """
    return 42

def think_too_much():
    """Express Caesar's skepticism about Cassius"""

    print("""Yond Cassius has a lean and hungry look,
He thinks too much; such men are dangerous.""")

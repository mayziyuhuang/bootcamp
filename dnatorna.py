"""Convert DNA sequence to RNA and the returned sequences are all upper case"""

def rna(seq):
    """Convert a DNA sequence to RNA and the returned sequences are all upper case"""

    #Convert to uppercase
    seq = seq.upper()

    return seq.replace('T', 'U')

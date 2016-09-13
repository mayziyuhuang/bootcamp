def find_all_starts(seq):
    """Find the starting index of all start codons in a lowercase seq"""
    # Initialize array of indices of start codons
    starts = []

    # Find index of first start codon (remember, find() returns -1 if not found)
    i = seq.find('atg')

    # Keep looking for subsequence incrementing starting point of search
    while i >= 0:
        starts.append(i)
        i = seq.find('atg', i + 1)

    return tuple(starts)


def find_first_in_register_stop(seq):
    """
    Find first stop codon on seq that starts at an index
    that is divisible by three
    """

    seq = seq.lower()

    # Scan sequence for stop codon
    i = 0
    while i < len(seq) - 2 and seq[i:i+3] not in ('taa', 'tag', 'tga'):
        i += 3

    # If before end, found codon, return end of codon
    if i < len(seq) - 2:
        return i + 3
    else: # Failed to find stop codon
        return -1


def all_orfs(seq):
    """Return all ORFs of a sequence."""
    # Make sure sequence is all lower case
    seq = seq.lower()

    # Find the indices of all start codons
    start_inds = find_all_starts(seq)

    # Keep track of stops
    stop_inds = []

    # Initialze ORFs.  Each entry in list is [ORF length, ORF start, ORF stop]
    orfs = []

    # For each start codon, find the next stop codon in register
    for start in start_inds:
        relative_stop = find_first_in_register_stop(seq[start:])

        if relative_stop != -1:
            # Index of stop codon
            stop = start + relative_stop

            # If already had stop, a longer ORF contains this one
            if stop not in stop_inds:
                orfs.append((relative_stop, start, stop))
                stop_inds.append(stop)

    # Get sorted list of ORF length
    orfs = sorted(orfs, reverse=True)

    # Remove lengths
    for i, orf in enumerate(orfs):
        orfs[i] = (orf[1], orf[2])

    return tuple(orfs)


def longest_orf(seq):
    """Longest ORF of a sequence."""
    orfs = all_orfs(seq)

    if len(orfs) == 0:
        return ''
    else:
        return seq[orfs[0][0]:orfs[0][1]]


# Compute it
#salmonella_orf = longest_orf(seq)

# Look at it
#salmonella_orf


def translate(seq):
    """Translate a DNA sequence into protein"""

    import bioinfo_dicts

    # Make sure sequence is upper case
    seq = seq.upper()

    # Find start codon
    i = 0
    while i < len(seq) + 2 and seq[i:i+3] != 'ATG':
        i += 1

    # Translate until the stop codon or end of string
    prot = []
    while i < len(seq) - 2 and seq[i:i+3] not in ('TAA', 'TGA', 'TAG'):
        prot.append(bioinfo_dicts.codons[seq[i:i+3]])
        i += 3

    return ''.join(prot)


#translate(salmonella_orf)


def longest_orf(seq, n=1):
    """Longest ORF of a sequence."""
    orfs = all_orfs(seq)

    if len(orfs) == 0:
        return ''
    elif n == 1 or len(orfs) == 1:
        return seq[orfs[0][0]:orfs[0][1]]
    else:
        return_list = []
        for i in range(min(n, len(orfs))):
            return_list.append(seq[orfs[i][0]:orfs[i][1]])
        return tuple(return_list)


# Compute ORFs
#orfs = longest_orf(seq, n=5)

# Translate them
#prots = []
#for orf in orfs:
#    prots.append(translate(orf))

# Make a FASTA file
#with open('sal_seqs.faa', 'w') as f:
#    for i, prot in enumerate(prots):
#        f.write('> {0:d}\n'.format(i))
#        f.write(prot + '\n')


#!cat sal_seqs.faa

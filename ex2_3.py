def gc_blocks(seq, block_size):

    """divides a sequence into blocks and computes the GC content"""

    GC_content = []
    group = len(seq)// block_size

    for i in range(0, block_size * group, block_size):
        sub_seq = seq[i:i+block_size]
        GC = (sub_seq.count('G')+sub_seq.count('C')) / block_size
        GC_content.append(GC)
        i += block_size-1

    return tuple(GC_content)

#exercise solution
#def gc_content(seq):
#    """GC content of a given sequence"""
#    seq = seq.upper()
#    return (seq.count('G') + seq.count('C')) / len(seq)

#def gc_blocks(seq, block_size):
#    """
#    Divide sequence into non-overlapping blocks
#    and compute GC content of each block.
#    """
#    blocks = []
#    for i in range(0, len(seq) - (len(seq) % block_size), block_size):
#        blocks.append(gc_content(seq[i:i+block_size]))
#    return tuple(blocks)


def gc_map(seq, block_size, gc_thresh):

    """GC content above threshold is capitalized and below the threshold is lowercase"""
    GC_tuple = gc_blocks(seq, block_size)
    seq_map = []

    for j in range(len(GC_tuple)):
        if GC_tuple[j] >= gc_thresh:
            sub = seq[j*block_size:(j+1)*block_size]
            new = sub.upper()
        else:
            sub = seq[j*block_size:(j+1)*block_size]
            new = sub.lower()
        seq_map.append(new)

    return ''.join (seq_map)

#exercise solution
#def gc_map(seq, block_size, gc_thresh):
#    """Give back seq with lowercase letters where GC content is low."""

#    out_seq = ''

    # Determine GC content of each block and change string accordingly
#    for i in range(0, len(seq) - (len(seq) % block_size), block_size):
#        if gc_content(seq[i:i+block_size]) < gc_thresh:
#            out_seq += seq[i:i+block_size].lower()
#        else:
#            out_seq += seq[i:i+block_size].upper()

#    return out_seq

#my solution for c and d
#with open('data/salmonella_spi1_region.fna', 'r') as f:
#    all_seq = ''
#    for line in f:
#        if line[0]!= '>':
#            all_seq = f.read()
#        seq_ex2 = all_seq.replace("\n", "")

#seq_ex3 = gc_map(seq_ex2, 1000, 0.45)

#with open('data/salmonella_spi1_region.fna', 'r') as f, open('ex2_3.fna', 'w') as f_out:
#    lines = f.readlines()
#    for line in lines:
#        if line[0] == '>':
#            f_out.write(line)
#    for j in range(0, len(seq_ex3), 60):
#        f_out.write(seq_ex3[j:j+60])
#        f_out.write("\n")

#exercise solution
# Write the result
#with open('salmonella_spi1_region_gc_map.fna', 'w') as f:
    # Write description text
#    f.write(descriptor + '\n')

    # Write sequence in blocks of 60
#    i = 0
#    while i < len(sal_gcmap) - 59:
#        f.write(sal_gcmap[i:i+60] + '\n')
#        i += 60

    # Write last line
#    f.write(sal_gcmap[i:])

#!head salmonella_spi1_region_gc_map.fna
#print('...')
#!tail salmonella_spi1_region_gc_map.fna

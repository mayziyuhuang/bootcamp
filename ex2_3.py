def gc_blocks(seq, block_size):

    """divides a sequence into blocks and computes the GC content"""
    GC_content = []

    for i in range(len(seq)+1):
        sub_seq = seq[i:i+block_size]
        GC = (sub_seq.count('G')+sub_seq.count('C')) / block_size
        i += block_size
        GC_content.append(GC)
        return GC_content

    return GC_content

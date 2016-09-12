def longest_common_substring(seqa, seqb):
    """Compute the longest common substring"""
    if len(seqa) < len(seqb):
        seq1 = seqa
        seq2 = seqb

        a = range(0, len(seq1)+1)
        alist = a[::-1]

        for i in alist:

            b = range(0, len(seq1)-i+1)
            blist = b[::-1]

            for j in b:
                if seq2.find(seq1[j:i]) != -1:
                    print(seq1[j:i])
                    break

            if seq2.find(seq1[j:i]) != -1:
                break

    else:
        seq1 = seqb
        seq2 = seqa
        a = range(0, len(seq1)+1)
        alist = a[::-1]

        for i in alist:

            b = range(0, len(seq1)+1)
            blist = b[::-1]

            for j in b:
                if seq2.find(seq1[j:i]) != -1:
                    print(seq1[j:i])
                    break

            if seq2.find(seq1[j:i]) != -1:
                break


    return

def longest_common_substring2(s1, s2):
    """Return one of the longest common substrings"""

    # Make sure s1 is the shorter
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    # Start with the entire sequence and shorten
    substr_len = len(s1)
    while substr_len > 0:
        # Try all substrings
        for i in range(len(s1) - substr_len + 1):
            if s1[i:i+substr_len] in s2:
                return s1[i:i+substr_len]

        substr_len -= 1

    # If we haven't returned, there is no common substring
    return ''

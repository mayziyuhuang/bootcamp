def longest_orf(seq):

    """ takea a DNA sequence as input and finds the lingest open reading frame"""
    #ORF : begins with ATG, ends with any of TGA, TAG, TAA, and total number of bases is a multile of 3

    #find ATG in seq
    start_list = find_seq(seq, 'ATG')

    #find TGA, TAG, TAA in seq
    end_list_1 = find_seq(seq, 'TGA')
    end_list_2 = find_seq(seq, 'TAG')
    end_list_3 = find_seq(seq, 'TAA')
    end_list = sorted(end_list_1 + end_list_2 + end_list_3)


    return start_list, end_list



def find_seq(seq, codon):
    """find ATG, TGA, TAG, TAA in the seq"""

    num_list = []
    for i in range(len(seq)):
        num = seq.find(codon, i, i+3)
        if num != -1:
            num_list.append(num)
        i += 1

    return num_list

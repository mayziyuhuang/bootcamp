import numpy as np
import re

def find_codon_lesson6(codon, seq):
    """Find a specified codon with a given sequence."""

    i = 0
    # Scan sequence until we hit the start codon or the end of the sequence
    while seq[i:i+3] != codon and i < len(seq):
        i += 1

    if i == len(seq):
        return -1

    return i


synapto_nuc = (
    "ATGGAGAACAACGAAGCCCCCTCCCCCTCGGGATCCAACAACAACGAGAACAACAATGCAGCCCAGAAGA"
    "AGCTGCAGCAGACCCAAGCCAAGGTGGACGAGGTGGTCGGGATTATGCGTGTGAACGTGGAGAAGGTCCT"
    "GGAGCGGGACCAGAAGCTATCGGAACTGGGCGAGCGTGCGGATCAGCTGGAGCAGGGAGCATCCCAGTTC"
    "GAGCAGCAGGCCGGCAAGCTGAAGCGCAAGCAATGGTGGGCCAACATGAAGATGATGATCATTCTGGGCG"
    "TGATAGCCGTTGTGCTGCTCATCATCGTTCTGGTGTCGCTTTTCAATTGA")

synapto_prot = (
    "MENNEAPSPSGSNNNENNNAAQKKLQQTQAKVDEVVGIMRVNVEKVLERDQKLSELGERADQLEQGASQF"
    "EQQAGKLKRKQWWANMKMMIILGVIAVVLLIIVLVSLFN")


print('ATG :', find_codon_lesson6('ATG', synapto_nuc))
print('AAT :', find_codon_lesson6('AAT', synapto_nuc))
print('TGT :', find_codon_lesson6('TGT', synapto_nuc))
print('TGC :', find_codon_lesson6('TGC', synapto_nuc))

print("M : ", synapto_prot.find("M"))
print("N : ", synapto_prot.find("N"))
print("C : ", synapto_prot.find("C"))

all_codons = re.findall('...', synapto_nuc)
print('ATG :', 'ATG' in all_codons)
print('AAT :', 'AAT' in all_codons)
print('TGT :', 'TGT' in all_codons)
print('TGC :', 'TGC' in all_codons)


# write up a new function
def find_codon_new(codon, seq):
    """Find a specified codon with a given sequence"""
    i = 0
    # Scan sequence until we hit the start codon or the end of the sequence
    while seq[i:i+3] != codon and i < len(seq):
        i += 3

    if i == len(seq):
        return -1

    return i

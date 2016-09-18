import pytest
import lesson36a

def test_find_codon(find_codon):
    """
    A function to test another function that looks for a codon
    within a coding sequence
    """
    synapto_nuc = (
        "ATGGAGAACAACGAAGCCCCCTCCCCCTCGGGATCCAACAACAACGAGAACAACAATGCAGCCCAGAAGA"
        "AGCTGCAGCAGACCCAAGCCAAGGTGGACGAGGTGGTCGGGATTATGCGTGTGAACGTGGAGAAGGTCCT"
        "GGAGCGGGACCAGAAGCTATCGGAACTGGGCGAGCGTGCGGATCAGCTGGAGCAGGGAGCATCCCAGTTC"
        "GAGCAGCAGGCCGGCAAGCTGAAGCGCAAGCAATGGTGGGCCAACATGAAGATGATGATCATTCTGGGCG"
        "TGATAGCCGTTGTGCTGCTCATCATCGTTCTGGTGTCGCTTTTCAATTGA")

    assert find_codon('ATG', synapto_nuc) == 0
    assert find_codon('AAT', synapto_nuc) == 54
    assert find_codon('TGT', synapto_nuc) == -1
    assert find_codon('TGC', synapto_nuc) == -1

    return None

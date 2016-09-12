codon = input('Type your codon:')
codon_list = ['UAA', 'UAG', 'UGA']
codon_tuple = tuple(codon_list)
if codon == 'AUG':
    print('This codon is the start codon.')
elif codon in codon_tuple:
    print('This codon is a stop codon.')
else:
    print('This codon is neither a start nor stop codon.')

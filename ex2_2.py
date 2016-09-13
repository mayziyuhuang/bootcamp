with open('data/salmonella_spi1_region.fna', 'r') as f:
    all_seq = ''
    for line in f:
        if line[0]!= '>':
            all_seq = f.read()
        seq_ex2 = all_seq.replace("\n", "")



#exrcise solution
# Read all the lines into a list
#with open('data/salmonella_spi1_region.fna', 'r') as f:
#    file_str = f.read()

# Cut off first line, but keep descriptor
#descriptor = file_str[:file_str.find('\n')]
#file_str = file_str[file_str.find('\n')+1:]

# Eliminate newlines
#seq = file_str.replace('\n', '')

# Take a look at the first 500 bases to make sure we got it right.
#seq[:500]

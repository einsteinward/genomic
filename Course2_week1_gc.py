#!/user/bin/python

# Multiple line comments are included in """......"""
"""
It computes the GC content of a DNA seq
"""

#Get DNA seq
dna = 'acgctcgcgcggcgatagctgatcgatcggcgcgcttttttttaaaag'
no_c = dna.count('c')         #Count C's in DNA seq
no_g = dna.count('g')         #Count G's in DNA seq
dna_length = len(dna)         #Get the length of DNA seq
gc_percent = (no_c + no_g)*100/dna_length    #Compute the GC%
print(gc_percent)             #Print GC% to screen

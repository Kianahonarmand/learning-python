Complementing a Strand of DNA 
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.
DNA = "AGTATGATCTATCTGAGGGGACTGTGAGCGAGCTTCGCAATGCGTGTATAACGTTTAGGTTATAATTGAACAAGCCATAGGCTTCCTATAAGCAAGGCTTCAAACCTTATTCGTCATCGTGGAATTCACAAGGTGTTTGGGCGTCTCATCTTGCCAATGACGGATACGCAGCGTGGCAACCATGCTCATTGCGGGGCTGGTCATTAACTCTGAGAGATCGAAGCGGACTCCGACGTTCCTCCTATTTCGAGTCATGTTTTTTAACGCAGCACCGGCCTTTATCAACGGCTATCGCCTTCTGAGTCGCGGTCAAGTAAGGGCCTAGTGAAGTTACGTCAAATTATCTCGCGGAATTATTGGTACACGAACGTCGAACGTTTAATCATATAAAGACGGAGAATTCCGGACACATGCTCGGTAAGGACGCCAATAAGTGTATTGCAAGAAAAGGATATAGGGAACACTTGATGGGGCAGCAGCCTTTTAGGCCCGACATGTCCCACCTTCAAGCACGCGGACGGAAAGCGTTTTTCAAGGATACTAGAAGCGCGAATACTAGGTTTAGTGGCTCGGTCGGATTAATCTTTCGCAAAAGCGGTGACTGTTCTTAGGATATGTGGCTCCCCGTTTCAAGGGGATGATGACTTGCCCCGGGGCGAACGTATACCTCCATGGCAAGTTAGAATGCGGACCGAGAGTATAGGAGCAGTCTCTTGGCTATCCACGTGTTTCCGCCCTAGGTGACTCGGCCAGAACCCTCGATAGATTGTAAAACCAGGCTACTCACTAAGGCTTGGAAGATAACCCA"
def dna_string(DNA):
    nucleotides = {"A" : "T", "C": "G"}
    complement = ""
    for nucleo in DNA:
        for key, value in nucleotides.items():
            if nucleo == key:
                complement += value
            elif nucleo == value:
                complement +=key
    return complement[::-1]
dna_string(DNA)

TGGGTTATCTTCCAAGCCTTAGTGAGTAGCCTGGTTTTACAATCTATCGAGGGTTCTGGCCGAGTCACCTAGGGCGGAAACACGTGGATAGCCAAGAGACTGCTCCTATACTCTCGGTCCGCATTCTAACTTGCCATGGAGGTATACGTTCGCCCCGGGGCAAGTCATCATCCCCTTGAAACGGGGAGCCACATATCCTAAGAACAGTCACCGCTTTTGCGAAAGATTAATCCGACCGAGCCACTAAACCTAGTATTCGCGCTTCTAGTATCCTTGAAAAACGCTTTCCGTCCGCGTGCTTGAAGGTGGGACATGTCGGGCCTAAAAGGCTGCTGCCCCATCAAGTGTTCCCTATATCCTTTTCTTGCAATACACTTATTGGCGTCCTTACCGAGCATGTGTCCGGAATTCTCCGTCTTTATATGATTAAACGTTCGACGTTCGTGTACCAATAATTCCGCGAGATAATTTGACGTAACTTCACTAGGCCCTTACTTGACCGCGACTCAGAAGGCGATAGCCGTTGATAAAGGCCGGTGCTGCGTTAAAAAACATGACTCGAAATAGGAGGAACGTCGGAGTCCGCTTCGATCTCTCAGAGTTAATGACCAGCCCCGCAATGAGCATGGTTGCCACGCTGCGTATCCGTCATTGGCAAGATGAGACGCCCAAACACCTTGTGAATTCCACGATGACGAATAAGGTTTGAAGCCTTGCTTATAGGAAGCCTATGGCTTGTTCAATTATAACCTAAACGTTATACACGCATTGCGAAGCTCGCTCACAGTCCCCTCAGATAGATCATACT


# How I solved it? First thing first, I ask for help from a friend who knows how to work with python. At first I wanted to slove it exactly like the way the flowchart was drawn. I mean, start writing for-loop with the contenct that if it's "A", then put "T" in the complement = '' and write down `elif` for all of the 4 nucleotides and it worked but as we worked with dictionaries I thought it might not be the answer that you wanted from us. For the reversing I used slicing because I checked it in 'w3schools' and it made more sense for me than using `.reverse()` in the for-loop.


# second solution with the sample dataset
DNA = "AAAACCCGGT"
def string(DNA):
    complement = ''
    for i in DNA:
        if i == "A":
            complement += "T"
        elif i == "T":
            complement += "A"
        elif i == "C":
            complement += "G"
        elif i == "G":
            complement += "C"
    return complement[::-1]
string(DNA)
'ACCGGGTTTT'
#
# to count the GC content, put all the(only) GC-nucleotides in a new string and calculate the amount of GC in each string. 
# also calculate all the amounts of nucleotides in the main strings with `len()` function.
# to get the percentage : 100*(calculated GC content / all the nucleotides in the main string)





def strand_DNA(DNA):
    GC_content = []
    for i in DNA:
        if i == "C":
            GC_content += "G"
        elif i == "G":
            GC_content += "C"
        else:
            continue
    return GC_content

Rosalind_6404 = "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
GC_Rosalind_6404 = len(strand_DNA("CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"))
Rosalind_5959 = "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
GC_Rosalind_5959 = len(strand_DNA("CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"))
Rosalind_0808 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
GC_Rosalind_0808 = len(strand_DNA("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"))
                    
result = GC_Rosalind_6404 * 100 / len(Rosalind_3699), GC_Rosalind_5959 * 100 / len(Rosalind_5959), GC_Rosalind_0808 * 100 / len(Rosalind_0808)
highest = max(result)
print(highest)
output = round(highest, 5)
print(output)

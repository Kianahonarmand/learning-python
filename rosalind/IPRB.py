# Mendel's First Law
# there are 3 populations: {'k': AA, 'm': Aa, 'n': aa}
# parents : kk , km, kn, mk, mm, mn, nk, nm, nn
# probability of having an offspring with at least one dominant allele and dominant phenotype. 
# counting the probability of picking each parent and having a dominant offspring:
k = 2
m = 2
n = 2
total = k + m + n 
probability_of_kParent = (k / total) * ((k - 1) / (total - 1)) + (k / total) * (m / (total - 1)) + (k / total) * (n / (total - 1))
probability_of_mParent = (m / total) * (k / (total - 1)) + 3/4*((m / total) * ((m - 1) / (total - 1))) + 1/2*((m / total) * (n / (total-1)))
probability_of_nParent = (n / total) * (k / (total - 1)) + 1/2*((n / total) * (m / (total - 1))) 
result = probability_of_kParent + probability_of_mParent + probability_of_nParent
print(result)
sample_dataset : k = 2     m = 2    n = 2            output = 0.7833333333333334
my_dataset : k = 20     m = 20    n = 30            output = 0.675983436853002
# to round it up by 0.00001
result = round(probability_of_kParent + probability_of_mParent + probability_of_nParent, 5)
print(result)     ===================> 0.67598
# Counting Point Mutation
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

def mutation_count(s,t):
    m = 0
    for i in range(0, len(t)):
        if s[i] == t[i]:
            continue
        else:
            m = m + 1
    return m 
print(mutation_count(s,t))

# at first s and t was defined. 
# then we write a for-loop for the length of the either strings that we have as they have the same amounts of characters.
# if-part: we say if the item in the s-string was the same as the item in t-string, ignore it; if not, count it as one in the mutation_count.
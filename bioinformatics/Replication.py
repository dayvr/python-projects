# Counts the number of times the specified pattern appears in the given text
def pattern_count(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count = count+1
    return count


# Computes the frequency map of a given string Text and integer k
def frequency_map(text, k):
    freq = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freq[pattern] = 0
        for j in range(n-k+1):
            if text[j:j+k] == pattern:
                freq[pattern] += 1
    return freq

# Another version of the algorithm above that not uses a nested loop and finds the most frequent k-mers in a string Text
def frequency_map2(text, k):
    freq = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        if pattern not in freq:
            freq[pattern] = 1
        else:
            freq[pattern] += 1
    return freq

# Find the most frequent occurrence of words in a given text
def frequent_words(text, k):
    words = []
    freq = frequency_map2(text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words

Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
k = 10

# Print the result of calling FrequentWords on Text and Pattern.
print(frequent_words(Text, k))

# Takes a string Pattern and returns a string formed  by reversing all the letters of Pattern
def reverse(pattern):
    rev = ""
    for i in range(len(pattern)):
        rev = pattern[i] + rev
    return rev

# One line version of the above function
def reverse2(pattern):
    return pattern[::-1]

# Using reversed()
def reverse3(pattern):
    return ''.join(reversed(pattern))


# Takes a DNA string Pattern and returns the complementary string of Pattern (with every nucleotide replaced by its complement)
def complement(pattern):
    comp = ""
    for i in range(len(pattern)):
        if pattern[i] == 'A':
            comp += 'T'
        elif pattern[i] == 'T':
            comp += 'A'
        elif pattern[i] == 'C':
            comp += 'G'
        elif pattern[i] == 'G':
            comp += 'C'
    return comp

# Find all occurrences of a pattern in a string
def pattern_matching(pattern, genome):
    positions = []
    for i in range(len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)] == pattern:
            positions.append(i)
    return positions
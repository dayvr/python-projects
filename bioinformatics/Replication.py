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
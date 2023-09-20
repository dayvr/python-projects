def pattern_count(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count = count+1
    return count


def frequency_map(text, k):
    frequency_map = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        frequency_map[pattern] = 0
    return frequency_map



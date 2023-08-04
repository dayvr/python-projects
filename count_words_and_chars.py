def count_words_and_characters(input_string):
    words = input_string.split()  # Split the input into words
    total_characters = sum(len(word) for word in words)  # Count characters in each word
    
    return len(words), total_characters

# Get user input
user_input = input("Enter a phrase: ")

# Call the function and print the results
word_count, character_count = count_words_and_characters(user_input)
print(f"Number of words: {word_count}")
print(f"Total number of characters: {character_count}")

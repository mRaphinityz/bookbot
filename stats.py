import sys
import os
sorted_freq = []

# Count the frequency of each character in the text
def book_string():
    input_value = sys.argv[1]
    with open(input_value) as f:
        text = f.read()
        word = text.split()
        return len(word)

# Sort the character frequency dictionary by frequency
def character_frequency(text: str) -> dict:
    input_value = sys.argv[1]
    freq_dict = {}
    with open(input_value) as f:
        text = f.read()
        for char in text.lower():
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    return freq_dict

# Print the sorted character frequency
def sort_stats():
    input_value = sys.argv[1]
    freq_dict = character_frequency(input_value)
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_freq.pop(0)
    for item in sorted_freq:
        print(f"{item[0]}: {item[1]}")



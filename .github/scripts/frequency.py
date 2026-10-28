import sys
from collections import Counter

def count_vowels(file_path):
    # Count how often each vowel appears in a text file
    vowels = "aeiou"
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
        counts = Counter(char for char in text if char in vowels)
        return counts
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        sys.exit(1)

if __name__ == "__main__":
    # The script needs exactly one argument: the file path
    if len(sys.argv) != 2:
        print("Usage: python3 frequency.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    result = count_vowels(file_path)
    print(result)
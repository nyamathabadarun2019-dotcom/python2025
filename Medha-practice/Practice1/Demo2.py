# Assignment 2: Word Frequency Counter

text = input("Enter a paragraph of text: ")

# Convert to lowercase to ignore case
text = text.lower()

# Remove punctuation manually
punctuations = ".,!?;:'\"()-[]{}"
for p in punctuations:
    text = text.replace(p, "")

# Split text into words
words = text.split()

# Create dictionary for counting
word_count = {}

# Count frequency of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Sort by frequency (descending)
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Display results
print("\nWord Frequency (Most frequent first):")
for word, count in sorted_words:
    print(f"{word}: {count}")

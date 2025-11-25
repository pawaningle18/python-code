# Input string from user
text = input("Enter a string: ").lower()

# Initialize counters
vowels = 0
consonants = 0

# Loop through each character
for char in text:
    if char.isalpha():  # Check if it's a letter
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Print results
print("Vowels:", vowels)
print("Consonants:", consonants)


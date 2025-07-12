# The user is asked to enter a sentence
str_manip = input("Enter a sentence: ")

# Get the amount of characters within the sentence
amount = len(str_manip)
sentence = f"The amount of characters is: {amount}" 
print(sentence)

# Find the last letter in the sentence
letter = str_manip[-1]
print(letter)

# Replace the last letter with a character @
print(str_manip.replace(letter, "@"))

# Print last 3 characters backwards
three = str_manip[-3:]
reverse = three[::-1]
sentence = f"The last three characters backwards are: {reverse} "
print(sentence)

#Create a 5-letter word that is made up of the first three letters and the last two letters.
first_three = str_manip[0:3]
print(first_three)
last_two = str_manip[-2:]
print(last_two)
word = first_three + last_two
print(word)



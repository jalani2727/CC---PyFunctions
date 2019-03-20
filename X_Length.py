# 1.
# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. This function should return True if every word in sentence has a length greater than or equal to x.

# Write your x_length_words function here:
def x_length_words(sentence, x):
  compare_to = sentence.split()
  for item in compare_to:
    if len(item) >= x:
      return True
    else:
      return False
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
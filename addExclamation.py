# 1.
# Create a function named add_exclamation that has one parameter named word. This function should add exclamation points to the end of word until word is 20 characters long. If word is already at least 20 characters long, just return word.


# Write your add_exclamation function here:
def add_exclamation(word):
  if len(word) < 20:
    i = len(word)
    while i < 20:
      word+= "!"
      i+=1
    return word
  else:
    return word
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
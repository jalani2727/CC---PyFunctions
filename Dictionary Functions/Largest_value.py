#Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.

# Write your max_key function here:
def max_key(my_dictionary):
  max_at_end = sorted(list(my_dictionary.values()))
  for item in my_dictionary:
    if my_dictionary[item] == max_at_end[-1]:
      return item
    else:
      continue
# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
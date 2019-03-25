#
#Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function should return the number of unique values in the dictionary.
#  Write your unique_values function here:
def unique_values(my_dictionary):
  new_list = []
  for value in list(my_dictionary.values()):
    if value in new_list:
      continue
    else:
      new_list.append(value)
  return len(new_list)
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1
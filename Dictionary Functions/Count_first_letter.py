#Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where the key is a last name and the value is a list of first names.The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.

# Write your count_first_letter function here:
def count_first_letter(names):
  empty_dict = {}
  for item in names:
    if item[0] in empty_dict:
      empty_dict[item[0]] += len(names[item])
    else:
      empty_dict[item[0]] = len(names[item])
    
  return empty_dict
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
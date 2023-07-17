# Description: Day 3 of 50 Days of Code: register check

# def register_check(dict: dict):
#   count = 0
#   for key in dict.values():
#     if key == "yes":
#       count += 1
      
#   return count

# register = {'Michael': 'yes', 'John': 'no','Mary':'yes'}

# print(register_check(register))

# Another way

def register_check(dict: dict):
  count = 0
  new_dict = {}
  for key, value in dict.items():
    if value == "yes":
      count += 1
      new_dict[key] = value
  return f'Number of student in school is {count} which are {new_dict}'

register = {'Michael': 'yes', 'John': 'no','Mary':'yes'}

print(register_check(register))


# Extra Challenge: Lowercase Names

import re

names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

def Lowercase_names(names : list):
  tuple = ()
  for name in sorted(names, reverse= True):
    if name.islower():
      tuple = tuple + (name,)
      
  return tuple


print(Lowercase_names(names))

# Description: Day 1 of 50 Days of Code: Division and Square-root
def divide_or_square(num):
  if num % 5 == 0:
    return num ** 0.5
  else:
    return num % 5
  
print(divide_or_square(10))

#Extra Challenge: Longest Value

def longest_value(dict):
  longest = 0
  for key in dict:
    if len(dict[key]) > longest:
      longest = len(dict[key])
      longest_key = dict[key]
  return longest_key

fruits = {'fruit': 'apple', 'color': 'green'}
print(longest_value(fruits))


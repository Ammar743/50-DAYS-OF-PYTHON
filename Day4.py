# Description: Day 4 of 50 Days of Code: Only Floats

def only_floats(a, b):
  if type(a and b) == float:
    return 2
  elif type(a or b) == float:
    return 1
  else:
    return 0
  
print(only_floats(2.0, 3.0))
print(only_floats(2.0, 3))
print(only_floats(2, 3))

# Extra Challenge: Index of the Longest Word

def word_index(strings: list):
  for string in strings:
    if all(len(string) == len(strings[0]) for string in strings):
      return 0
  else:
    return f'The index of the longest word is: {strings.index(max(strings, key=len))}'
    
print(word_index(["hi", "hello", "welcome"]))
print(word_index(["welcome", "goodbye"]))
# Description: Day 2 of 50 Days of Code: Strings to Integers

def convert_add(list):
  new_list = []
  for i in list :
    i = int(i)
    new_list.append(i)
  return f'The sum is: {sum(new_list)}'

print(convert_add(["1", "3", "5"]))

#Extra Challenge: Duplicate Names

def duplicate_names(list: list):
  duplicate = []
  for i in list:
    if list.count(i) > 1:
      if i not in duplicate:
        duplicate.append(i)

  if duplicate:  
    return f'The duplicate list is: {duplicate}'
  else:
    return 'No duplicates found'

fruits = ['apple', 'orange', 'banana', 'apple', 'banana']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
print(duplicate_names(fruits))
print(duplicate_names(names))

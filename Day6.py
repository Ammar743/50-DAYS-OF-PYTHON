# Description: Day 5 of 50 Days of Code:  User Name Generator

def user_name():
  email = input("Enter your email: ")
  userName = email.split('@')[0]
  return userName

print(user_name())

# Extra Challenge: Zero Both Ends

def zeroed(numbers : list):
  numbers[0], numbers[-1] = 0, 0
  return numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(zeroed(numbers))
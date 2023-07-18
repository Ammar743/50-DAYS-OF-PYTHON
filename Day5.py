# Description: Day 5 of 50 Days of Code:  My Discount

def my_discount():
  price = int(input("Enter the price of the item: "))
  discount = int(input("Enter the discount: "))
  priceAfterTheDiscount = price - (price * (discount / 100))
  print(f'The price after the discount is: {priceAfterTheDiscount}')


# Extra Challenge: Tuple of Student Sex

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 
'female']
def count_students(students: list):
  
  

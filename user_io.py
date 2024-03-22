import inventory as i

# A function that gets the user's input of money and validates it
def get_money():
  money = float(input("How much money do you have? "))
  return money
  

# A function that displays the list of items and gets the user's choice of item
def get_choice():
  choice = input("What would you like? ")
  return choice
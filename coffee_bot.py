#Here's the coffee bot code
def coffee_bot():
  
  #Simple Greeting
  print("Welcome to the cafe!")
  order_drink = 'y'
  drinks = []
  
  # Loop to allow more than one drink in the order
  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()
    cup_type = get_cup_type()

    drink = '{} {} {}'.format(size, drink_type, cup_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)
    
    while True:
      order_drink = input("Would you like to order another drink? (y/n)? \n")
    
      if order_drink == 'y' or 'n':
        break

  print("Okay so I have: ")

  for drink in drinks:
    print('-', drink)

  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))

#Functions for selecting specifics about the drinks

#Function for telling the program what size to get the drink in
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print("Please select [a], [b], or [c]")
    get_size()

#Another function for the type
def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n")
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print("Please select [a], [b], or [c]")
    get_drink_type()

#If the user selects a latte, this function is used
def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n')
  if res == 'a':
    return 'Mocha with 2% milk'
  elif res == 'b':
    return 'Mocha with Non-fat milk'
  elif res == 'c':
    return 'Mocha with Soy milk'
  else:
    print("Please select [a], [b], or [c]")
    order_latte()

# Function used to select cup type
def get_cup_type():
  res = input('And what kind of cup would you like that served in? \n[a] Plastic Cup \n[b] Reusable Cup \n[c] Paper Cup \n')
  if res == 'a':
    return 'in a plastic cup'
  elif res == 'b':
    return 'in a reusable cup'
  elif res == 'c':
    return 'in a paper cup'
  else:
    print("Please select [a], [b], or [c]")

# If the user orders a mocha, this function is activated
def order_mocha():
  while True:
    res = input("Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n")
    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'

#Calling Mr.Bot, please
coffee_bot()
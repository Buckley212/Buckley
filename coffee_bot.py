#Here's the coffee bot code
def coffee_bot():
  
  #Simple Greeting
  print("Welcome to the cafe!")
  
  #
  size = get_size()
  drink_type = get_drink_type()
  cup_type = get_cup_type

  print("Alright, that's a {} {} in a {}!".format(size, drink_type, cup_type))
  
  name = input("Can I get your name please? \n")
  
  print("Thanks, {}! Your drink will be ready shortly.".format(name))

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

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n")
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'b':
    return 'Mocha'
  elif res == 'c':
    return order_latte()
  else:
    print("Please select [a], [b], or [c]")
    get_drink_type()
  
def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n')
  if res == 'a':
    return '2% milk'
  elif res == 'b':
    return 'Non-fat milk'
  elif res == 'c':
    return 'Soy milk'
  else:
    print("Please select [a], [b], or [c]")
    order_latte()

def get_cup_type():
  res = input('And what kind of cup would you like that served in? \n[a] Plastic Cup \n[b] Reusable Cup \n[c] Paper Cup \n')
  if res == 'a':
    return 'Plastic Cup'
  elif res == 'b':
    return 'Reusable Cup'
  elif res == 'c':
    return 'Paper Cup'
  else:
    print("Please select [a], [b], or [c]")
# Call coffee_bot()!
coffee_bot()

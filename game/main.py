import random

def choose_options():
  options=("piedra","papel","tijeras")
  user_option=input("priedra, papel o tijeras =>")
  user_option=user_option.lower()

  if not user_option in options:
    print("Esa opcion no es valida")
    return None, None
  
  computer_option = random.choice(options)
  return user_option, computer_option

def rules_game(user_option, computer_option):
  if user_option == computer_option:
    return -1
  elif user_option=="piedra" and computer_option=="tijeras":
    return 1
  elif user_option=="papel" and computer_option=="piedra":
    return 1
  elif user_option=="tijeras" and computer_option=="papel":
    return 1
  else:
    return 0

def run_game():
  computer_wins=0
  user_wins=0
  rounds=1
  while True:
    print("*"*10)
    print("ROUND", rounds)
    print("*"*10)    
    print("computer_wins", computer_wins)
    print("user_wins", user_wins)
    
    user_option, computer_option = choose_options()

    if user_option != None and computer_option != None:
      print("user choose", user_option)
      print("computer choose", computer_option)
      rounds+=1
      
      result_game= rules_game(user_option, computer_option)
      if result_game == 1:
        user_wins+=1
      elif result_game == 0:
        computer_wins+=1
      
      if user_wins == 2:
        print("Winer is User!!!", user_wins)
        break
      
      if computer_wins == 2:
        print("Winer is Computer!!!", computer_wins)
        break

run_game()
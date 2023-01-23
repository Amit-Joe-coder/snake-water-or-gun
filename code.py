import random
lst=['s','w','g']
noof_chances=0
chances=5
computer=0
player=0
print("\t\t\t---SnaKe,WaTer and Gun---\t\t\t")
print("-Enter s for snake\n-Enter w for water\n-Enter g for gun\n")
print("Total Chance One Get Are 5")
while noof_chances<chances:
  _input=input('\t\t~~~snake,water,gun:')
  _random=random.choice(lst)

  if _input==_random:
    print("This is Draw")
    print(f"computer chooses {_random} and player chooses {_input}")

  #user input s
  elif _input=="s" and _random=="w":
    print(f"Player wins by choosing {_input}\n")
    print(f"Computer looses by choosing {_random}\n")
    player+=1
  elif _input=="s" and _random=="g":
    print(f"computer wins by choosing {_random}\n")
    print(f"player looses by choosing {_input}\n")
    computer+=1

  #user input w
  elif _input=="w" and _random=="s":
    print(f"computer wins by choosing {_random}\n")
    print(f"player looses by choosing {_input}\n")
    computer+=1
  elif _input=="w" and _random=="g":
    print(f"computer looses by choosing {_random}\n")
    print(f"player wins by choosing {_input}\n")
    player+=1

  #user input g
  elif _input=="g" and _random=="w":
    print(f"Player looses by choosing {_input}\n")
    print(f"Computer wins by choosing {_random}\n")
    computer+=1
  elif _input=="g" and _random=="s":
    print(f"computer looses by choosing {_random}\n")
    print(f"player wins by choosing {_input}\n")
    player+=1
  noof_chances+=1
  print(f"\t+++You only left with {chances-noof_chances} chances+++")
if player==computer:
  print("_________Tie_______")
elif player>computer:
  print(f"_________Player wins by {player} points__________")
else:
  print(f"________Computer wins by {computer} points________")

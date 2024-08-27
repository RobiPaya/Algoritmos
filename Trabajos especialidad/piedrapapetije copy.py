import random
lita=["rock","paper","scissors"]
ia=random.choice(lita)
print(ia)
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

opcion=input("PAPE, rok, sisor: ").upper()

for x in lita:
    if opcion in x:
        opcion=x

if ia>opcion:
    print("ganaste")
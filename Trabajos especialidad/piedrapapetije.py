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

opcion=input("PAPE, rock, sisor: ").lower()

for x in lita:
    if opcion in x:
        opcion=x
print(opcion)
if ia=="rock" and opcion=="paper":
    print("ganaste")
elif ia=="rock" and opcion=="scissor":
    print("Peridns")
elif ia=="scissors" and opcion=="paper":
    print("perdiste")
elif ia=="scissors" and opcion=="rock":
    print("Ganaste")
elif ia=="paper" and opcion=="rock":
    print("Perdiste")
elif ia=="paper" and opcion=="scissors":
    print("Ganaste")
else:
    print("empate")

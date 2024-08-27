import random
lita=["rock","paper","scissors"]
ia=random.choice(lita)

rocky = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

papery = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissorsy = """

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
    print(f"Diego : {rocky}\n Tu: {papery}")
    print("ganaste")
elif ia=="rock" and opcion=="scissor":
    print(f"Diego : {rocky}\n Tu: {scissorsy}")
    print("Peridns")
elif ia=="scissors" and opcion=="paper":
    print(f"Diego : {scissorsy}\n Tu: {papery}")
    print("perdiste")
elif ia=="scissors" and opcion=="rock":
    print(f"Diego : {scissorsy}\n Tu: {rocky}")
    print("Ganaste")
elif ia=="paper" and opcion=="rock":
    print(f"Diego : {papery}\n Tu: {rocky}")
    print("Perdiste")
elif ia=="paper" and opcion=="scissors":
    print(f"Diego : {papery}\n Tu: {scissorsy}")
    print("Ganaste")
else:
    print("empate UwU")
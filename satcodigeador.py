from os import system
system('cls')
import random
dibujos={
    'Goku': 50,
    'Vegeta': 40,
    'Krilin': 1,
    'Freezer': 20,
    'Bulma': 200
    }
Goku=random.randint(1,40)
Vegeta=random.randint(1,35)
Krilin=random.randint(1,20)
Freezer=random.randint(1,40)
Bulma=random.randint(1,50)
DG=Goku*dibujos.get("Goku")
DV=Vegeta*dibujos.get("Vegeta")
DK=Krilin*dibujos.get("Krilin")
DF=Freezer*dibujos.get("Freezer")
DB=Bulma*dibujos.get("Bulma")
Total=DG+DV+DK+DF+DB
Multa=300*Total/100
Pobreza=Total-Multa
print(f"Las ganado es :{Total}")
print(f"La multa del sat es de :{Multa}")
print(f"Lo que se debe es :{Pobreza}")
Dibujos={"Goku":50,"Vegeta":40,"Krilin":1,"Freezer":20,"Bulma":200}

Goku=9
Vegeta=23
Krilin=7
Freezer=5
Bulma=6

TG=Goku*Dibujos.get("Goku")
TV=Vegeta*Dibujos.get("Vegeta")
TK=Krilin*Dibujos.get("Krilin")
TF=Freezer*Dibujos.get("Freezer")
TB=Bulma*Dibujos.get("Bulma")

TotalDinero=TG+TV+TK+TF+TB
MultaSAT=300*TotalDinero/100
Deuda=MultaSAT-TotalDinero

print(f"Las ganancias totales son {TotalDinero}")
print(f"La multa del sat es de {MultaSAT}")
print(f"La deuda final esa de {Deuda}")
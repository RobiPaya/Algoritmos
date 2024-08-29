cont=0
palbara=input("PALABRA: ").lower().strip()
for x in palbara:
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        cont+=1
print(f"EL total de vocales son {cont}")

lista=["VERDADERO","FALSO"]
print('Roberto doesn´t know how to speak english ')
a=input("Verdadero/Falso").upper()
for x in lista:
    if a in x:
        a=x

if a=="VERDADERO":
    print("CORRECTO")
else:
    print("INCORRECTO")
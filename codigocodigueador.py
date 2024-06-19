lista=["VERDADERO","FALSO"]
print('Roberto doesn´t know how to speak english ')
a=input("Verdadero/Falso").upper()
for x in lista:
    if a in x:
        if a=="VERDADERO":
            print("Verda")
        else:
            print("falso")
    else:
        print("Callate Roberto")
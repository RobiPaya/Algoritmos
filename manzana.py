peso=int(input("Peso : "))
cianuro=int(input("MG : "))
if peso<50 or peso>120 or cianuro<1:
    print("eror")
else:
    if cianuro/peso>3:
        print(cianuro-peso*3)
    else:
        print("SEGURO")

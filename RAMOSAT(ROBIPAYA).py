entrada='''10 gokus
1 vegeta
1 krilin
90 bulmas
1 freezer'''.replace("s","").split()
total=0
for x in entrada:
    if x.isnumeric():
        a=int(x)
    else:
        if x=="goku":
            total+=a*50
        elif x=="krilin":
            total+=a
        elif x=="vegeta":
            total+=a*40
        elif x=="freezer":
            total+=a*20
        else:
            total+=a*200

print(f"Total de ingresos: {total}\nMulta del SAT: {total*3}\nDeuda: {total*3-total}")







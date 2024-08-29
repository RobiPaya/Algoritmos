lista=[1,2,3,4,5,6,7,8,9,10]
lista.reverse()
organizado=""
cotna=0
for x in lista:
    if x==1:
        cotna+=1
    else:
        organizado+=str(x)+","
print(f"{organizado}1")
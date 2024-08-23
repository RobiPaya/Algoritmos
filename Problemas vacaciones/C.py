numerodelugares=int(input("Cuántos lugares van a darle like? : "))
likes=[]
lugar=0
a=0
for totaldenumerodelugares in range(numerodelugares):
    lugar+=1
    likes.append(int(input(f"Cuántos likes para el lugar {lugar}? : ")))
maximo=(max(likes))
for x in likes:
    b=x
    if x==maximo:
        print(maximo)
        b=-1
        for nose in range(b-a):
            print("X")
            break
    else:
        a+=1
        print("X")

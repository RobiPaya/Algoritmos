palabra=input("Dame una palabra: ").lower()
inversa=palabra[::-1]
if palabra==inversa:
    print("Es una palbra polindroma")
else:
    print("no")
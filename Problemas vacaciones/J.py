entrada='''5
P A
G E
G M
P K
G D
'''.split()
cont=0
for x in entrada:
    if x=="G":
        print(entrada[cont],entrada[cont+1])
    cont+=1
if not "G" in entrada:
    print("0")
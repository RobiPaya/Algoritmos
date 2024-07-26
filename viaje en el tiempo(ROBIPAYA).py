entrada='''4820
7
'''.split()
entrada[0]=int(entrada[0])
entrada[1]=int(entrada[1])
if entrada[0]>3500:
    if entrada[1]<=10:
        entrada[0]=entrada[0]*0.5
print(entrada[0])

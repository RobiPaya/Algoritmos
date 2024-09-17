from fucniones import *
lado=int(input("Lado : "))

print(f"""Cuadrado : {areacuadrado(lado)}
triángulo : {areatriangulorectangulo(lado):.0f}
Hexágono regualar : {areaheaxa(lado)}
circulo : {areacircul(lado):.2f}
pentagono regular : {areapentagono(lado)}""")
from fucniones import *
lado=int(input("Lado : "))

print(f"""Cuadrado : {areacuadrado(lado)}
triángulo : {areatriangulorectangulo(lado):.0f}
rectraugnulo : {areaheaxa(lado)}
circulo : {areacircul(lado):.2f}
semiciruclo : {areapentagono(lado)}""")
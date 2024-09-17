import math 

def areacuadrado(lado):
    return lado * lado

def areatriangulorectangulo(lado):
    return (lado*lado)/2

def areaheaxa(lado):
    base=int(input("Base : "))
    return (base*lado)

def areacircul(lado):
    return 3.1416 * (lado/2)**2

def areapentagono(lado):
    return (3.1416 * (lado/2)**2)/2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:14:17 2021

@author: franco
"""
def validar_rut(rut):
   
    #tomo el rut y lo dividdo
    rut = rut.replace(".", "")
    splitrut = rut.split("-")
    #el digitos contiene el rut y dv el verificador
    digitos = list(splitrut[0])
    dv = splitrut[1]
    dv = dv.upper()
    #inicializo las variables
    i=2
    s=0
    #recorro el digitos en reversa
    #Realizo la operacion del algoritmo
    for digito in reversed(digitos):
        if i > 7:
            i = 2
        d = int(digito)
        s = ((d*i) + s)
        i += 1

    rf = (11-(s%11))
    #Compraro el resultado para asignar resultado
    if rf == 11:
        rf="0"
    elif rf == 10:
        rf="K"
    else:
        rf=str(rf)

    #Conmparo el rf con el dv para verificar el rut
    if dv == rf:
        return True
    else:
        return False
   

    


def mayusculas(cadena, indice=0):
    if indice == len(cadena):
        return []
        
    if cadena[indice].isupper():
        return [(cadena[indice], indice)] + mayusculas(cadena, indice+1)
    else:
        return mayusculas(cadena, indice+1)
    
cadena = "HolaSapoBiENoQuE"
resultado = mayusculas(cadena)

print(resultado)
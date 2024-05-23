nombre = [1, 2, 3, 4, 5]

def multiplication_liste(nombre):
    retour = []
    for number in nombre :
        retour.append(number * 2)
    return retour

def multiVMAXSHINNY(liste):
    return [ x*2 for x in liste]

nombre = multiVMAXSHINNY(nombre)
print(nombre)

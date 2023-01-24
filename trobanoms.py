import random
from silabesNomsPropis import silabesPropisMin as silabes
from combinacions import incompatibles 
#variables
nom = []
llargada = random.choice([1,1,2,2,2,2,3,3,3,4])
#funcions
def obtenirLletres():
    darrera = nom[-2][-1]
    primera = nom[-1][0]
    return "{}".format(darrera + primera)

def compatibilitat():
    if obtenirLletres() in incompatibles:
        global nom
        nom = nom[ : -1]
        afegirSilaba()
    
def afegirSilaba():
    nom.append(random.choice(silabes))

def crearNom():
    for x in range (llargada):
        if len(nom) == 0:
            afegirSilaba()
        else:
            afegirSilaba()
            compatibilitat()
#crides

with open ("noms.txt", "w") as noms:
    for i in range (10):
        crearNom()
        noms.write("".join(nom) + "\n")
        print(nom)
        nom.clear()




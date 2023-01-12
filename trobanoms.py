import random
from silabes import silabes
from combinacions import incompatibles 
#variables
nom = []
llargada = random.choice([1,1,2,2,2,2,2,2,2,3])
#funcions
def obtenirLletres():
    darrera = nom[-2][-1]
    primera = nom[-1][0]
    return "{}".format(darrera + primera)

def compatibilitat():
    if obtenirLletres() in incompatibles:
        global nom
        print(obtenirLletres())
        nom = nom[ : -1]
        afegirSilaba()
    
def crearNom():
    nom.append(random.choice(silabes))
    print(nom)

def afegirSilaba():
    crearNom()
    compatibilitat()
#crides
for x in range (llargada):
    if len(nom) == 0:
        crearNom()
    else:
        afegirSilaba()
#output
print(nom)


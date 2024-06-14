import json
import os

# Chemin vers le fichier JSON
fichier_json = os.path.join('data', 'object.json')


# Ouverture et lecture du fichier
with open(fichier_json, 'r') as fichier:
    data = json.load(fichier)

# Affichage des données désérialisées
print(data)


class Personnage:

    countID = 0
    
    def __init__(self, data):
        
        self.__name = data.get('name','Monstre')
        self.__hp = int(data.get('hp','5'))
        self.__attack = int(data.get('attack','5'))
        self.__critHit = 5

   


    def getName(self):
        return self.__name


    def getID(self):
        return self.__id
    
    def getAttack(self):
        return self.__attack
    
    def getHp(self):
        return self.__hp
    
# Création des listes d'instance
monstres = [Personnage(obj) for obj in data['mobs']]

bo = monstres[0]
ca = monstres[1]
pro = monstres[2]
pi = monstres[3] 
hug = monstres[4] 


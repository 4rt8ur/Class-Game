import json

# Chemin vers le fichier JSON
fichier_json = 'C:\Users\arthu\Documents\PERSO\PROJECTS\Class-Game\object.json'

# Ouverture et lecture du fichier
with open(fichier_json, 'r') as fichier:
    donnees = json.load(fichier)

# Affichage des données désérialisées
print(donnees)


class Personnage:

    countID = 0
    
    def __init__(self, name, hp=100, attack=100):
        
        self.__name = name
        self.__hp = hp
        self.__attack = attack
        self.__critHit = 5
        self.__id = Personnage.countID
        Personnage.countID+=1

   


    def getName(self):
        return self.__name


    def getID(self):
        return self.__id
    
    def getAttack(self):
        return self.__attack
    
    def getHp(self):
        return self.__hp
    
    def setName(self, new):
        self.__name = new
    

hugo = Personnage(input("nom :"))
objets = [caca, pipi, prout]
class Jeu :
    def __init__(self, objets):
        self.items = objets
                
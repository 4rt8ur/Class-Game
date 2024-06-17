import json
import os

# Chemin vers le fichier JSON
fichier_json = os.path.join('data', 'object.json')


# Ouverture et lecture du fichier
with open(fichier_json, 'r') as fichier:
    data = json.load(fichier)

# Affichage des données désérialisées
print(data)

###-----------------------------------------------------------------------------------------###

# Création d'une classe Personnage pour créer les monstres et le personnage principale
class Personnage:

    def getName(self):
        return self._name

    def getID(self):
        return self._id
    
    def getAttack(self):
        return self._attack
    
    def getHp(self):
        return self._hp
    
    def getCritHit(self):
        return self._critHit
    
#------------------- Sous Class ------------------------    
class Monstres(Personnage):
    
    def __init__(self, data):
    
        self._name = data.get('name','Monstre')
        self._hp = int(data.get('hp','5'))
        self._attack = int(data.get('attack','5'))
        self._critHit = 5
    
class Joueur(Personnage):
    
    def __init__(self, nom):
        
        self._name = nom
        self._hp = 5
        self._attack = 3
        self._critHit = 5
        self._money = 0
        self._object = False
        
    def getMoney(self):
        return self._money

#--------------------------------------------------------- Class pour les objets --------------------------------------------------
class Object :
    def __init__(self, data):
        pass
        
        self._name = data.get('name','objet')
        self._hp = int(data.get('hp','0'))
        self._attack = int(data.get('attack','0'))
        self._critHit = int(data.get('critHit','0'))
        self._cost = int(data.get('money','10'))

# ------------------------------------------------------------------- Création du personnage principal ----------------------------------------

principal_character = Joueur(input("Entrer votre nom : "))

print(principal_character.getName())

#-------------------------------------------------------------------- Création des listes d'instance -----------------------------------------

monstres = [Monstres(obj) for obj in data['mobs']] # 5 instances(mobs) dans la liste

boss = [Monstres(obj) for obj in data['boss']] # 3 instances(boss) dans la liste

objects = [Object(obj) for obj in data['objects']] # 20 instances(objets) dans la liste

#-------------------------------------------------------------------------- Class Jeu ------------------------------------------------------------


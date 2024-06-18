# coding: utf-8

import json
import os

# Clear le terminal 
os.system("cls")

# Chemin relatif vers le fichier JSON
fichier_json = os.path.join('data', 'object.json')


# Ouverture et lecture du fichier
with open(fichier_json, 'r') as fichier:
    data = json.load(fichier)


###-----------------------------------------------------------------------------------------###

# Création d'une classe Personnage pour créer les monstres et le personnage principale
class Personnage:
    
    def __init__(self, name):
        self._name = name
        self._critHit = 5

    def getName(self):
        return self._name
    
    def getAttack(self):
        return self._attack
    
    def getHp(self):
        return self._hp
    
    def getCritHit(self):
        return self._critHit
    
#------------------- Sous Class ------------------------    
class Monstres(Personnage):
    
    def __init__(self, data):
        super().__init__(data.get('name','Monstre'))
        self._hp = int(data.get('hp','5'))
        self._attack = int(data.get('attack','5'))
    
class Joueur(Personnage):
    
    def __init__(self, nom):
        super().__init__(nom)
        self._hp = 5
        self._attack = 3
        self._money = 0
        self._object = None 
        
    def getMoney(self):
        return self._money

#--------------------------------------------------------- Class pour les objets --------------------------------------------------
class Object :
    def __init__(self, data):
        self._name:     str = data.get('name','objet')
        self._hp:       int = int(data.get('hp','0'))
        self._attack:   int = int(data.get('attack','0'))
        self._critHit:  int = int(data.get('critHit','0'))
        self._cost:     int = int(data.get('cost','10'))
    
    def getName(self):
        return self._name
    
    def getCost(self):
        return self._cost

# ------------------------------------------------------------------- Création du personnage principal ----------------------------------------

principal_character = Joueur(input("Entrer votre nom : "))

print(principal_character.getName())

#-------------------------------------------------------------------- Création des listes d'instance -----------------------------------------

monstres = [Monstres(obj) for obj in data['mobs']] # 5 instances(mobs) dans la liste

boss = [Monstres(obj) for obj in data['boss']] # 3 instances(boss) dans la liste

objects = [Object(obj) for obj in data['objects']] # 20 instances(objets) dans la liste

#-------------------------------------------------------------------------- Class Jeu ------------------------------------------------------------

class Jeu :
    def __init__(self, monstres, boss, character, objects):
        self._monstre = monstres
        self._boss = boss
        self._joueur = character
        self._objects = objects
        
    def openStore(self):
        #for i in range(20):
          #  print(jeu.getNameobjects(i),"/" ,jeu.getCost(i),"")
        for obj in self._objects:
            print(obj.getName(), " -> ", obj.getCost(), "€")
        
    def getCost(self, i):
        return self._objects[i]._cost
        
    def getNameobjects(self, i):
        return self._objects[i]._name
    
    def getNameMonstre(self, i):
        return self._monstre[i]._name

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#_________________________________________________________________________________________________________________________________________________________________________________________#

jeu = Jeu(monstres, boss, principal_character, objects)

jeu.openStore()



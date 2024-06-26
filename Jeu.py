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
        self._gears = []
        
    def getMoney(self):
        return self._money
    
    def getName(self):
        return self._name
    
    def addGear(self, gear):
        self._gears.append(gear)
        
    def getGears(self):
        return self._gears
        
        

#--------------------------------------------------------- Class pour les objets --------------------------------------------------

class Object :
    
    id = 0
    def __init__(self, data):
        
        
        self._name:     str = data.get('name','objet')
        self._hp:       int = int(data.get('hp','0'))
        self._attack:   int = int(data.get('attack','0'))
        self._critHit:  int = int(data.get('critHit','0'))
        self._cost:     int = int(data.get('cost','10'))
        self._id:       int = Object.id
        Object.id += 1
        
        
    
    def getName(self):
        return self._name
    
    def getCost(self):
        return self._cost

    def getId(self):
        return self._id
# ------------------------------------------------------------------- Création du personnage principal ----------------------------------------





verification = input("Entrez votre nom : ")
space_detector = verification.find(" ")

print("\n-Votre nom doit comporter au moins 1 caractère .\n-Il ne peut pas posséder d'espace .\n")

while len(verification) == 0 or space_detector > -1:
    
    verification = input("Entrez votre nom : ")
    space_detector = verification.find(" ")
    

        

principal_character = Joueur(verification)

#-------------------------------------------------------------------- Création des listes d'instance -----------------------------------------

monstres = [Monstres(obj) for obj in data['mobs']] # 5 instances(mobs) dans la liste

boss = [Monstres(obj) for obj in data['boss']] # 3 instances(boss) dans la liste

gears = [Object(obj) for obj in data['objects']] # 20 instances(objets) dans la liste

#-------------------------------------------------------------------------- Class Jeu ------------------------------------------------------------

class Jeu :
    def __init__(self, monstres, boss, character, objects):
        self.monstres = monstres
        self.boss = boss
        self.joueur = character
        self.gear = gears
        
        
            
        
    

    def openStore(self):
        #for i in range(20):
          #  print(jeu.getNameobjects(i),"/" ,jeu.getCost(i),"")
        os.system("cls")
        print("\nBienvenue dans le magasin",self.joueur.getName(),"!\n")
        
        compteur_action = 0
        for obj in self.gear:
            compteur_action += 1
            print(obj.getId(), obj.getName(), " -> ", obj.getCost(), "€")
            
            
        print(compteur_action, "Quitter le magasin")
        
        action = int(input("Que voulez vous faire ? Entrez le numéro correspondant à l'action voulue :\n"))
        if action == compteur_action:
            pass
        else :
            self.joueur.addGear(self.gear[action])
            
        for obj in self.joueur.getGears():
            print(obj.getName())
            
        
        
            
        
        
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#_________________________________________________________________________________________________________________________________________________________________________________________#

jeu = Jeu(monstres, boss, principal_character, gears)

jeu.openStore()


print("C'est bon ")
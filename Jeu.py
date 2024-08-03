# coding: utf-8
import json
import os
import time
import re

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
        self._money:  int = int(100)
        self._gears = []
        
    def getMoney(self):
        return self._money
    
    
    
    def addGear(self, gear):
        self._gears.append(gear)
        
    def getGears(self):
        return self._gears
    
    def setMoney(self, gear_paid):
        self._money = self._money - gear_paid
        return self._money
    
        
        

#--------------------------------------------------------- Class pour les objets --------------------------------------------------

class Object :
    
    id = 0
    def __init__(self, data):
        
        
        self._name:     str = data.get('name','objet')
        self._hp:       int = int(data.get('hp','0'))
        self._attack:   int = int(data.get('attack','0'))
        self._critHit:  int = int(data.get('critHit','0'))
        self._cost:     int = int(data.get('cost','10'))
        self._possede       = False
        self._id:       int = Object.id
        Object.id += 1
        
        
    
    def getName(self):
        return self._name
    
    def getCost(self):
        return self._cost

    def getId(self):
        return self._id
    
    def getAttack(self):
        return self._attack
    
    def getHp(self):
        return self._hp
    
    def getObtention(self):
        return self._possede
    
    def setObtention(self, objet_traite, liste):
        
        for obj in liste:
            if objet_traite == obj :
                objet_traite._possede = True
        
    
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
        
        
            
    def openMenu(self):
        menu_ouvert = True
        while menu_ouvert : 
            print("\nBonjour", self.joueur.getName(),"!\n")
            print("\n0 - Aller au magasin\n1 - Aller combattre")
            endroit = input("Où voulez vous aller ?\n")
            
            verif = re.match(r'\d',endroit)
            if verif != None:

                endroit = int(endroit)     
                
                if endroit == 0 :
                    menu_ouvert = None
                    self.openStore()
                    
                elif endroit == 1 :
                    menu_ouvert = None
                    self.openCombat()
            
                else :
                    print("Choisir entre 0 et 1")
                    self.openMenu()

            else :
                print("Invalide")


        
        

        
        
        
        
            

    
    def openCombat(self):
        print("Bienvenue dans le ring !!")
        print("Que voulez vous combattre parmi :\n")

        for monstre in self.monstres :
            print("- ", monstre.getName(),"/", monstre.getAttack(),"Attaque /", monstre.getHp(),"Hp")

        cible = input()

        



    
    def combat(self, target):
        pass



    def openStore(self):
        ouverture_magasin = True
        while ouverture_magasin :
        
            #for i in range(20):
            #  print(jeu.getNameobjects(i),"/" ,jeu.getCost(i),"")
            os.system("cls")
            for obj in self.gear:
                obj.setObtention(obj, self.joueur.getGears())
            
            print("\nBienvenue dans le magasin",self.joueur.getName(),"!\n")
            print("Vous avez :", self.joueur.getMoney(), "€")
            for obj in self.joueur.getGears():
                
                print("Vous possédez le", obj.getName())
            
            compteur_action = 0
            for obj in self.gear:
                compteur_action += 1
                if obj.getObtention() == True:
                    print(obj.getId(), obj.getName(), " -> ", obj.getCost(), "€ /  Obtenu")
                else:
                    print(obj.getId(), obj.getName(), " -> ", obj.getCost(), "€")

                
                
            print(compteur_action, "Quitter le magasin")
            
            action = input("Que voulez vous faire ? Entrez le numéro correspondant à l'action voulue :\n")
            
            
            verification = re.match(r'\d',action)
            
            if verification == None :
                print(f"Vous devez entrez un nombre entre 0 et {compteur_action}")
                time.sleep(2)
                continue
            
            action = int(action)

            if action > compteur_action:
                print(f"Vous devez entrez un nombre entre 0 et {compteur_action}")
                time.sleep(2)
                continue

            
            if action == compteur_action:
                print("T'as quitté\n")
                ouverture_magasin = False
                self.openMenu()
                
            
            elif self.gear[action].getObtention():
                print("Vous avez déjà cet objet")
                time.sleep(1)
                continue

            elif self.joueur.getMoney() >= self.gear[action].getCost():
            
                self.joueur.addGear(self.gear[action])
                
                print("Vous avez :", self.joueur.setMoney(self.gear[action].getCost()), "€")
                
            
            else :
                print("Vous n'avez pas assez d'argent")
                time.sleep(2)
                
            
            
            
            
           
            
           
        
    
        
            
        
        
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#_________________________________________________________________________________________________________________________________________________________________________________________#

jeu = Jeu(monstres, boss, principal_character, gears)

jeu.openMenu()

print("C'est bon ")
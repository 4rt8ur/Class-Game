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
    
    id = 0
    def __init__(self, data):
        super().__init__(data.get('name','Monstre'))
        self._hp = int(data.get('hp','5'))
        self._attack = int(data.get('attack','5'))
        self._etat = False
        self._id:       int = Monstres.id
        Monstres.id += 1
        
    def getId(self):
        return self._id
    
    def setEtat(self):
        self._etat = True
    
    def getEtat(self):
        return self._etat
    
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
        boss_vaincu = 0
        nombre_boss = 0
        for boss in self.boss:
            nombre_boss += 1
            if boss.getEtat() == True:
                boss_vaincu += 1
                
        if boss_vaincu == nombre_boss:
            print("T'as battu tous les boss, t'as termine mon jeu")    
               
        else:    
            menu_ouvert = True
            while menu_ouvert : 
                print("\nBonjour", self.joueur.getName(),"!\nLe but du jeu est de vaincre tous les boss. Tu peux voir ta progression dans le menu pour battre les boss.")
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
        ring_open = True
        while ring_open:
            os.system("cls")
            liste_id = []
            print("Bienvenue dans le ring !!")
            print("Que voulez vous combattre :\n0 - Monstres \n1 - Boss")
            choix_type = input()
            if choix_type == "0":
                os.system("cls")
                for monstre in self.monstres :
                    print(monstre.getId(), "- ", monstre.getName(),"/", monstre.getAttack(),"Attaque /", monstre.getHp(),"Hp")
                    liste_id.append(monstre.getId())
                
                
                i = input("Entrez le numero du monstre voulu :")
                
                verif_syntaxe = re.match(r'\d', i)
                if verif_syntaxe != None:
                    
                    i = int(i)
                    verif_nombre = None
                    
                    for ids in liste_id:
                        if i == ids:
                            verif_nombre = True
                    
                    if verif_nombre == True :
                        target = self.monstres[i]        
                        ring_open = None  
                        self.combat(target)
                    
                    else:
                        print("Invalide")
                else:
                    print("Invalide")
                    
                              
            
            elif choix_type == "1":
                os.system("cls")
                for boss in self.boss :
                    if boss.getEtat() == True:
                        print(boss.getId(), "- ", boss.getName(),"/", boss.getAttack(),"Attaque /", boss.getHp(),"Hp / battue")
                    else :
                        print(boss.getId(), "- ", boss.getName(),"/", boss.getAttack(),"Attaque /", boss.getHp(),"Hp")
                    liste_id.append(boss.getId())
                    
                i = input("Entrez le numero du boss voulu :")
                
                verif_syntaxe = re.match(r'\d', i)
                if verif_syntaxe != None:
                    
                    i = int(i)
                    verif_nombre = None
                    
                    for ids in liste_id:
                        if i == ids:
                            verif_nombre = True
                    
                    if verif_nombre == True :
                        target = self.boss[i - 5] # i - 5 car dans la création, les monstres sont mis avant et donc ont les premiers id       
                        ring_open = None  
                        self.combat(target)
                    
                    else:
                        print("Invalide")     
            else :
                print("Invalide")
                
            
            
            
                    
        

        



    
    def combat(self, monstre):
        os.system("cls")
        print("Tu combats", monstre.getName())
        attaque_joueur = self.joueur.getAttack()
        hp_joueur = self.joueur.getHp()
        hp_monstre = monstre.getHp()
        for obj in self.joueur.getGears():
            attaque_joueur += obj.getAttack()
        
        print(attaque_joueur, hp_joueur, hp_monstre)
            
        combat = True    
        while combat == True:
            os.system("cls")
            print("Tu attaque :")
            hp_monstre -= attaque_joueur
            print(f"le monstre perd {attaque_joueur} Hp, il a donc {hp_monstre} Hp")
            if hp_monstre > 0:
                print("Le monstre attaque :")
                hp_joueur -= monstre.getAttack()
                print(f"Tu perds {monstre.getAttack()} Hp, tu as donc {hp_joueur} Hp")
            
            if hp_joueur <= 0:
                print("t'as perdu")
                time.sleep(2)
                os.system("cls")
                combat = False
                self.openMenu()
            
            elif hp_monstre <= 0:
                print("t'as win")
                time.sleep(2)
                os.system("cls")
                monstre.setEtat()
                combat = False
                self.openMenu()
            
            
        
                
                
            
        



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
                time.sleep(1)
                os.system("cls")
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
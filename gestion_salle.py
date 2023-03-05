#  ce script concerne un mini projet realise en python
# date de realisation 8 février 2023 : Encadrant: Abdelhamid zerrai
# Gestion de salle : les compétences visés : fonctions |les boucles |les conditions|lecture et ecriture des fichier |dictionnaires et les listes:

# creation de l'interface console :
import json

def affichMenu():
    print("*****************************************************************")
    print("=====               GESTION des Salles                      ===== ")
    print("*****************************************************************")
    print("=====   1- Nouvelle salle")
    print("=====   2- Lister toutes les salles")
    print("=====   3- Enregister les salles dans un fichier")
    print("=====   4- Quitter")
    print("*****************************************************************")

salle = {}
salles = []
prog=True
# boucle de la console
while(prog):
    affichMenu()
    choix = int(input(" >>>> Taper votre choix : >> \t"))
    if (choix == 1):
        # Ajout d'une nouvelle salle comme dictionnaire et ajouter dans une liste
        idsalle = int(input("Entrer numero de Salle : "))
        Typesalle = input("enter le type de salle : ")
        capacitsalle = int(input(" enter le capacite de la salle : "))
        salle.update({"IdSalle": idsalle})
        salle.update({"Type": Typesalle})
        salle.update({"Capacite": capacitsalle})
        salles.append(salle)
        print("-----------------------Fin de la saisie : (ok)")
        print("vouler vous ajouter un un autre salle ? Taper ( Y ) si oui ? Taper (O) si non ? :")
        respo=input()
        if(respo=='Y'):
            idsalle = int(input("Entrer numero de salle : "))
            Typesalle = input("enter le type de salle :")
            capacitsalle = int(input(" enter le capacite de la salle : "))
            salle={}
            salle.update({"IdSalle": idsalle})
            salle.update({"Type": Typesalle})
            salle.update({"Capacite": capacitsalle})
            salles.append(salle)
        else:
            prog=True

    elif (choix == 2):
        print("-------------------- LISTES DES SALLES -----------------------")
        print("|\t+ IdSalle |\t Type \t| Capacité \n")
        for sal in salles:
            print(f"\t+{sal['IdSalle']} |\t {sal['Type']} \t| {sal['Capacite']}")
            print("-------------------------------------------------------------")

        print("=====================================================================")
        print("________________ liste des salle enrengistré dans le fichier : \n")
        print("|\t+ IdSalle |\t Type \t| Capacité \n")

        with open('salles.txt','r') as f:
            classdonee = json.load(f)

        print(f"\t* {classdonee['IdSalle']} |\t {classdonee['Type']} \t| {classdonee['Capacite']}")








        continue
    elif(choix == 3):
        print("vouler vous enregister tous les salles dans le fichier : ")
        resp = input("si oui Taper (O) ? ou (N) pour non ?")
        if(resp=="O"):
            with open('salles.txt','a') as f:
                for i in salles:
                    json.dump(i, f)








    elif(choix == 4):
        print("\nFin de operation")
        prog = False







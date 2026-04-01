taches =["debut"]
def verif_num_entree_menu(num_entree):
    try:
        valeur = int(num_entree)
        if valeur < 5 and valeur != 0:
            print("on va dans le jeu")
            print( valeur)
            return valeur
        else:
            print("Entrée invalide. Le chiffre ne correspond pas au choix")    

    except:
        print("Entrée invalide. veuillez rentrer le bon chiffre")    


def instruction_choix_menu():
    nom_utilisateur= input("Quelle est votre nom \n" )

    print(f"\n bienvenue dans gestion de liste {nom_utilisateur}  !")
    print ("""Voici les options, choississez en entrant le chiffre attribuer:

            1 - Ajouter un élément 
            2 - Supprimer un élément
            3 - Afficher la liste
            4 - Quitter
        """)
    num_entree = input("Saisissez votre choix:\n" )
    return num_entree


def action(num) :
    print("youpi 0")
    if num== 1:
        print("youpi 1")
        tache = input("Saisissez la tache à mettre dans la liste" )
        taches.append(tache)
    elif num== 2: 
        
        tache = input("Saisissez la tache  à supprimer de la liste" )
        if tache in taches:
            taches.remove(tache)
        else:
            print(f"La tâche '{taches}' qui est à supprimer n'existe pas dans la liste")
    elif num==3:
        print(taches)
    




def menu():

    while True :
        num_entree = instruction_choix_menu()
        num = verif_num_entree_menu(num_entree)
        if num_entree ==4:
            break
        else: 
            bool = num_entree.isdigit()
            print(f"l'action va être appliquer avec num_entree = {num_entree} et bool = {bool}")
            action(num)
        



menu()

